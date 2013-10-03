(function($){
$.fn.updateMap = function(error, state, counties) {
	
	var firstKey = function(obj) {
    for (var a in obj) return a;
	}

	var width = Math.max(1100,document.documentElement["clientWidth"]),
	    height = 780,
	    margin = {top: 20, right: 20, bottom: 30, left: 130}, centered;

	var projection = d3.geo.albersUsa()
		.scale(1070)
		.translate([width / 2 + margin.left, height / 2]);
		
	var rateById = d3.map();

	var quantize = d3.scale.quantize()
	    .domain([0, .15])
	    .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

	var path = d3.geo.path()
		.projection(projection);

	var g;

	var bucketDict = assignBucketsToCounties(counties)

	var svg = d3.select("#interactiveMap").append("svg")
		.attr("width", width)
		.attr("height", height)
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	svg.append("rect")
		.attr("class", "background")
		.attr("width", width)
		.attr("height", height)

	g = svg.append("g")

	g.append("g")
	    .attr("class", "counties")
	    .selectAll("path")
	    .data(topojson.feature(state, state.objects[firstKey(state.objects)]).features)
	    .enter().append("path")
	    .attr("class", function(d) {
	    	var bucket = bucketDict[d.properties.NAME10.toUpperCase()];
	      	return "q" + (bucket ? bucket.fields.bucket : 0) + "-9"; 
	      })
	    .attr("d", path);

	g.selectAll('path').each(function(d){
        $(this).popover({trigger:'hover', title:d.properties.NAME10, placement:'top', content:"content", container:"body"});
    });

	var centroid = path.centroid(topojson.feature(state, state.objects[firstKey(state.objects)]));
	var x = centroid[0];
	var y = centroid[1];
	var k = 3;
    g.transition()
		      .duration(750)
		      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")");

}
})(jQuery);
