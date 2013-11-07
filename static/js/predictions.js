var updatePredictionChart = function(predictions) {

	var formatPrediction = function(prediction) {
		var baseDate = new Date();
		baseDate.setFullYear(2013,1,1);
		var startDate=new Date();
		startDate.setFullYear(2013,1,1);
		var data = [];
		var calcNum = function(date, prediction) {
			var x = (+date - +baseDate)/(1000*60*60*24);
			var y = parseFloat(prediction.fields.theta4) + 
				parseFloat(prediction.fields.theta3) * x +
				parseFloat(prediction.fields.theta2) * x * x +
				parseFloat(prediction.fields.theta1) * x * x * x +
				parseFloat(prediction.fields.theta0) * x * x * x * x;
			return y;
		}
		for (var i = 0; i <= 100; i++) {
			var d = {};
			var currDate = new Date();
			currDate.setTime(startDate.getTime() + 86400000*10*i);
			d.date = currDate;
			d.num = calcNum(d.date, prediction);
			data.push(d);
		}
		return data;
	};

	var data = formatPrediction(predictions[0]);

	var margin = {top: 20, right: 20, bottom: 30, left: 120},
    	width = 450 - margin.left - margin.right,
    	height = 250 - margin.top - margin.bottom;

	var x = d3.time.scale()
	    .range([0, width]);

	var y = d3.scale.linear()
	    .range([height, 0]);

	x.domain(d3.extent(data, function(d) { return d.date; }));
	y.domain(d3.extent(data, function(d) { return d.num; }));

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left");

	var line = d3.svg.line()
	    .x(function(d) { return x(d.date); })
	    .y(function(d) { return y(d.num); });
	
	var svg = d3.selectAll("#predictions").append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	svg.append("g")
	  .attr("class", "x axis")
	  .attr("transform", "translate(0," + height + ")")
	  .call(xAxis);

	svg.append("g")
	  .attr("class", "y axis")
	  .call(yAxis)
	.append("text")
	  .attr("transform", "rotate(-90)")
	  .attr("y", 6)
	  .attr("dy", ".71em")
	  .style("text-anchor", "end")
	  .text("Number of cases (#)");

	svg.append("path")
	  .datum(data)
	  .attr("class", "path_predict")
	  .attr("d", line);
};