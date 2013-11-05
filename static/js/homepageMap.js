var centered;
var projection = d3.geo.albersUsa();
var path = d3.geo.path().projection(projection);

	var g;
	var zipcodeNodes;
	var bucketDict;
	var pathDict;

var updateMap = function(error, us, states) {
	var width = 780;
	var height = 600;
	var margin = {top: 20, right: 20, bottom: 30, left: 130};
		
	var rateById = d3.map();

	var quantize = d3.scale.quantize()
	    .domain([0, 80])
	    .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));
	
	var quantizeState = d3.scale.quantize()
		.domain([0, 80])
		.range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

	projection.scale(950)
		.translate([width / 2, (height - 100)/ 2])

	bucketDict = assignBuckets(states);
	pathDict = assignPaths(topojson.feature(us, us.objects.state).features);

	var svg = d3.select("#interactiveMap").append("svg")
		.attr("width", width)
		.attr("height", height)
		//.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	svg.append("rect")
		.attr("class", "background")
		.attr("width", width)
		.attr("height", height)
		.on("click", clicked);

	g = svg.append("g");
	zipcodeNodes = svg.append("g");

	g.append("g")
	    .attr("class", "states")
	    .selectAll("path")
	    .data(topojson.feature(us, us.objects.state).features)
	    .enter().append("path")
	    .attr("class", function(d) {
	    	var bucket = bucketDict[d.properties.STUSPS10];
	      	return "q" + (bucket ? bucket.fields.bucket : 0) + "-9"; 
	      })
	    .attr("d", path)
	  	.on("click", function(d) { return clicked(d, width, height); });


	g.selectAll('path').each(function(d){
		var percentage = '0';
		var state = bucketDict[d.properties.STUSPS10];
		if (state) {
			percentage = '' + (state.fields.num_cases * 100 / bucketDict['US']) ;
		}
		var rateOfSpread = 
			!bucketDict[d.properties.STUSPS10] ? 'Not Spreading'
			: bucketDict[d.properties.STUSPS10].fields.bucket > 8 ? 'Rapid'
			: bucketDict[d.properties.STUSPS10].fields.bucket > 5 ? 'Fast'
			: bucketDict[d.properties.STUSPS10].fields.bucket > 2 ? 'Slow'
			: 'Not Spreading';
		var content = '<strong>Percentage of reported cases:</strong> ' + percentage.substring(0,5) + '%<br />';
		content += '<b>Rate of Spread: </b> ' + rateOfSpread;
        $(this).popover({trigger:'hover', html:"true", title:d.properties.NAME10, placement:'top', content:content, container:"body"});
    });
}

var handleCounty = function(centered, x, y, k, width, height) {
	if (centered) {
		var counties;

		d3.json("/countyjson/" + centered.properties.STUSPS10, function(json) {
			counties = json;
			d3.json("/static/data/" + centered.properties.STUSPS10 + ".json", function(state) {
		  		var zipcodes = zipcodeNodes.selectAll('path')
			  		.data(topojson.feature(state, state.objects[firstKey(state.objects)]).features);

			  	var countyDict = assignBucketsToCounties(counties);

		    	zipcodes.enter()
		    		.append("path")
		      		.attr("class", function(d) {
				    	var bucket = countyDict[d.properties.NAME10.toUpperCase()];
				      	return "q" + (bucket ? bucket.fields.bucket : 0) + "-9"; 
				     })
		    		.attr("d", path)
		    		.attr('stroke-width', 0.25)
		    		.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
				  	.on("click", function(d) { return clicked(d, width, height); });
		  		
		  		zipcodeNodes.selectAll('path').each(function(d){
					var percentage = '0';
					var state = countyDict[d.properties.NAME10.toUpperCase()];
					if (state) {
						percentage = '' + (state.fields.num_cases * 100 / countyDict['STATE']) ;
					}
					var rateOfSpread = 
						!countyDict[d.properties.NAME10.toUpperCase()] ? 'Not Spreading'
						: countyDict[d.properties.NAME10.toUpperCase()].fields.bucket > 8 ? 'Rapid'
						: countyDict[d.properties.NAME10.toUpperCase()].fields.bucket > 5 ? 'Fast'
						: countyDict[d.properties.NAME10.toUpperCase()].fields.bucket > 2 ? 'Slow'
						: 'Not Spreading';
					var content = '<strong>Percentage of reported cases:</strong> ' + percentage.substring(0,5) + '%<br />';
					content += '<b>Rate of Spread: </b> ' + rateOfSpread;
			        $(this).popover({trigger:'hover', html:"true", title:d.properties.NAME10, placement:'top', content:content, container:"body"});
			    });


		  	});
		  	
		});
	}
	else {
		zipcodeNodes.selectAll('path').data([]).exit().remove();
		d3.select("#ageDistribution").selectAll('svg').data([]).exit().remove();
		d3.select("#genderSplit").selectAll('svg').data([]).exit().remove();
		d3.select("#chart").selectAll('svg').data([]).exit().remove();
	}
};

var clicked = function(d, width, height) {
	var x, y, k;
	//window.location.replace("/state/" + d.properties.STUSPS10);
	//return;

	// if zooming in on state
	if (d && centered !== d && d.properties.STUSPS10) {
		centered = null;
		handleCounty(centered, x, y, k, width, height);
	    
	    var centroid = path.centroid(d);
	    x = centroid[0];
	    y = centroid[1];
	    k = 4;
	    if (d.properties.STUSPS10 == 'CA') k = 3;
	    if (d.properties.STUSPS10 == 'TX') k = 3;
	    centered = d;
	    
		$("#nationalTrends").css("display", "none");
		$("#stateTrends").fadeIn(2000);
		$("#mapTitle").css("visibility", "hidden");
		handleStats(d);
		handleCounty(centered, x, y, k, width, height);	
	  } 
	
	// clicking on a county
	/*else if (d && centered != d) {
		var county = d.properties.NAME10;
		queue()
		    .defer(d3.json, "/countygenderjson/" + county)
		    .defer(d3.json, "/countyagejson/" + county)
		    .defer(d3.json, "/countytimegraphjson/" + county)
			.await( 
				function(genderInfo, ageInfo, timeMessages) {
					updateGenderAndAge(error, genderInfo, ageInfo);
					updateTimeChart(timeMessages);
				}
			);
	}*/
	
	// if zooming out
	else {
	    x = width / 2;
	    y = height / 2;
	    k = 1;
	    centered = null;
		handleCounty(centered, x, y, k, width, height);
		$("#stateTrends").css("display", "none");
		$("#nationalTrends").fadeIn(2000);
		$("#mapTitle").css("visibility", "visible");
	}

	  g.selectAll("path")
	      .classed("active", centered && function(d) { return d === centered; });

	  g.transition()
	      .duration(750)
	      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
	      .style("stroke-width", 1.5 / k + "px");
	

}

var handleStats = function(stateObj) {
	var state = stateObj.properties.STUSPS10;
	document.getElementById("stateName").innerHTML=stateObj.properties.NAME10
	queue()
	    .defer(d3.json, "/static/data/" + state + ".json")
	    .defer(d3.json, "/countyjson/" + state)
	    .defer(d3.json, "/genderjson/" + state)
	    .defer(d3.json, "/agejson/" + state)
	    .defer(d3.json, "/statetimegraphjson/" + state)
	    .defer(d3.json, "/topmetrics/" + state)
	    .await(readyState);
};

var readyState = function(error, stateJson, counties, genderInfo, ageInfo, timeMessages, metrics) {
	var data = metrics[0].fields;
	document.getElementById("worstZipcode").innerHTML=data.worstZipcode;
	document.getElementById("numRecentCases").innerHTML=data.numRecentCases + ' new cases';
	document.getElementById("percentIncrease").innerHTML=data.percentIncrease + '%';
	updateGenderAndAge(error, genderInfo, ageInfo);
	updateTimeChart(timeMessages);
};

var handleZipcodeClick = function() {
	entry = document.getElementById("zipSearchBox").value;
	if (entry) {
		var yea = clicked(d3.json("/find/"+entry));
		console.log(yea);
	}
};

var searchClick = function() {
  	var width = 780;
	var height = 600;
	var search = document.getElementById("zipSearchBox").value;
  if (search) {
    var d = pathDict[search.toUpperCase()];
    if (d) clicked(d, width, height);
  }
};

