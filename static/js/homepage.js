var width = Math.max(910,document.documentElement["clientWidth"]),
    height = 500,
	centered;

var projection = d3.geo.albersUsa()
	.scale(1070)
	.translate([width / 2, height / 2]);
	
var rateById = d3.map();

var quantize = d3.scale.quantize()
    .domain([0, .15])
    .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

var path = d3.geo.path()
	.projection(projection);

queue()
    .defer(d3.json, "static/data/us_states_topo.json")
    .defer(d3.json, "/zipcodesjson")
    .await(ready);

var g;
function ready(error, us, states) {

	var bucketDict = assignBuckets(us.objects.state.geometries, states)
	
	var svg = d3.select("#interactiveMap").append("svg")
		.attr("width", width)
		.attr("height", height);

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
	  	.on("click", clicked);
}

function clicked(d) {
	var x, y, k;

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
}