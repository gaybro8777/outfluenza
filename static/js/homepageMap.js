(function($){
$.fn.updateMap = function(error, us, states) {
	var width = Math.max(1100,document.documentElement["clientWidth"]),
	    height = 700,
	    margin = {top: 20, right: 20, bottom: 30, left: 130}, centered;

	var projection = d3.geo.albersUsa()
		.scale(1070)
		.translate([width / 2 + margin.left, (height - 100)/ 2]);
		
	var rateById = d3.map();

	var quantize = d3.scale.quantize()
	    .domain([0, .15])
	    .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

	var path = d3.geo.path()
		.projection(projection);

	var g;
	var zipcodeNodes;

	var bucketDict = assignBuckets(states);
	
	var svg = d3.select("#interactiveMap").append("svg")
		.attr("width", width)
		.attr("height", height)
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

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
			: bucketDict[d.properties.STUSPS10].fields.bucket > 7 ? 'Rapid'
			: bucketDict[d.properties.STUSPS10].fields.bucket > 2 ? 'Slow'
			: 'Not Spreading';
		var content = '<strong>Percentage of reported case:</strong> ' + percentage.substring(0,5) + '%<br />';
		content += '<b>Rate of Spread: </b> ' + rateOfSpread;
        $(this).popover({trigger:'hover', html:"true", title:d.properties.NAME10, placement:'top', content:content, container:"body"});
    });

    var handleZipcodes = function(centered, x, y, k) {
		if (centered) {
		  	d3.json("/static/data/" + centered.properties.STUSPS10 + ".json", function(state) {
		  		zipcodeNodes.selectAll('g')
			  		.data(topojson.feature(state, state.objects[firstKey(state.objects)]).features)
		    		.enter()
		    		.append("path")
		    		.attr("class", function(d) {
		    			var bucket = bucketDict[d.properties.ZCTA5CE10];
		      			return "q" + (bucket ? bucket.fields.bucket : 2) + "-9"; 
		      		})
		    		.attr("d", path)
		    		.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
				  	.on("click", function(d) { return clicked(d, width, height); });
		  	});
		}
	};

	var clicked = function(d, width, height) {
		var x, y, k;
		//window.location.replace("/state/" + d.properties.STUSPS10);
		
		if (d && centered !== d) {
		    var centroid = path.centroid(d);
		    x = centroid[0];
		    y = centroid[1];
		    k = 3;
		    centered = d;
		  } else {
		    x = width / 2;
		    y = height / 2;
		    k = 1;
		    centered = null;
		  }

		  g.selectAll("path")
		      .classed("active", centered && function(d) { return d === centered; });

		  g.transition()
		      .duration(750)
		      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
		      .style("stroke-width", 1.5 / k + "px");
		handleZipcodes(centered, x, y, k);	
	}

}
})(jQuery);
