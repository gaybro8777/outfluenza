(function($){
$.fn.updateMap = function(error, us, messages) {
	var width = Math.max(1100,document.documentElement["clientWidth"]),
	    height = 700,
	    margin = {top: 20, right: 20, bottom: 30, left: 130}, centered;

    var numberFormat = d3.format(".2f");

    var usChart = dc.geoChoroplethChart("#interactiveMap");
    var genderChart = dc.pieChart("#genderChart");
    //var roundChart = dc.bubbleChart("#round-chart");

    var collectData = function (csv) {
    	console.log(csv[0])
        var data = crossfilter(csv);
		
        var states = data.dimension(function (d) {
            return d.fields.state;
        });
        
        var stateRaisedSum = states.group().reduceSum(function (d) {
            return 1;
        });
		
        var genders = data.dimension(function (d) {
            return d.fields.patientGender;
        });
        var statsByGender = genders.group().reduceSum(function (d) {
            return 1;
        });

        /*var rounds = data.dimension(function (d) {
            return d["RoundClassDescr"];
        });
        var statsByRounds = rounds.group().reduce(
                function (p, v) {
                    p.amountRaised += +v["Raised"];
                    p.deals += +v["Deals"];
                    return p;
                },
                function (p, v) {
                    p.amountRaised -= +v["Raised"];
                    if (p.amountRaised < 0.001) p.amountRaised = 0; // do some clean up
                    p.deals -= +v["Deals"];
                    return p;
                },
                function () {
                    return {amountRaised: 0, deals: 0}
                }
    	);*/
    	
        usChart.width(1090)
            .height(700)
            .dimension(states)
            .group(stateRaisedSum)
            .colors(["#ccc", "#DEEBF7", "#C6DBEE", "#9ECAE1", "#6BAED6", "#4292C6", "#2171B5", "#08519C", "#08306B", "#082854"])
            .colorDomain([-5, 200])
            .overlayGeoJson(us.features, "state", function (d) {
                return d.properties.name;
            })
            .title(function (d) {
            	//console.log(d)
                return "State: " + d.key + "\nTotal Amount Raised: " + 0 + "M";
            });

        genderChart.width(200)
        	.height(200)
        	.transitionDuration(500)
    		.dimension(genders) // set dimension
    		.group(statsByGender)

        dc.renderAll();
    };
	collectData(messages);

	d3.selectAll('path').attr('class', 'line');

/*
	var temp = function(error, us, states) {
	

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

	g = svg.append("g")

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
	}

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
	}*/

}
})(jQuery);
