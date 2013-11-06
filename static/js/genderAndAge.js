updateGenderAndAge = function(error, gender, ageInfo) {
	/* Age distribution chart */
	var margin = {top: 20, right: 20, bottom: 30, left: 40},
	    width = 450 - margin.left - margin.right,
	    height = 260 - margin.top - margin.bottom;
	 
	var formatPercent = d3.format(".0%");
	 
	var x = d3.scale.ordinal()
	    .rangeRoundBands([0, width], .1, 1);
	 
	var y = d3.scale.linear()
	    .range([height, 0]);
	 
	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");
	 
	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left")
	    .tickFormat(function(d) { return d; });
	 
	var svg = d3.selectAll("#ageDistribution").append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
	 
	var displayAge = function(error, data) {
		var total = 0;
	  data.forEach(function(d) {
	    d.frequency = d.frequency ? d.frequency : 0;
	    total += d.frequency;
	  });
	 
	  x.domain(data.map(function(d) { return d.age; }));
	  y.domain([0, d3.max(data, function(d) { 
	  	if (d) return d.frequency; 
	  	else return 0;
	  })]);
	 
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
	      .text("Frequency");
	 
	  var svgdata = svg.selectAll(".bar")
	      .data(data);

	  svgdata.enter().append("rect")
	      .attr("class", "bar")
	      .attr("x", function(d) { return x(d.age); })
	      .attr("width", x.rangeBand())
	      .attr("y", function(d) { return y(d.frequency); })
	      .attr("height", function(d) { return height - y(d.frequency); });
	  
	  
	 
	  d3.select("input").on("change", change);
	 
	  var sortTimeout = setTimeout(function() {
	    d3.select("input").property("checked", true).each(change);
	  }, 2000);
	 
	  function change() {
	    clearTimeout(sortTimeout);
	 
	    // Copy-on-write since tweens are evaluated after a delay.
	    var x0 = x.domain(data.sort(this.checked
	        ? function(a, b) { return b.frequency - a.frequency; }
	        : function(a, b) { return d3.ascending(a.age, b.age); })
	        .map(function(d) { return d.age; }))
	        .copy();
	 
	    var transition = svg.transition().duration(750),
	        delay = function(d, i) { return i * 50; };
	 
	    transition.selectAll(".bar")
	        .delay(delay)
	        .attr("x", function(d) { return x0(d.age); });
	 
	    transition.select(".x.axis")
	        .call(xAxis)
	      .selectAll("g")
	        .delay(delay);
	  }
	};
	var ages = [];
	for (var i = 0; i < 10; i++) {
		ages[i] = {'age':(i*10)+'-'+(i*10+9), 'frequency':0};
	}
	for (var i = 0; i < ageInfo.length; i++) {
		var key = Math.floor(ageInfo[i].pk/10);
		var age = ages[key];
		if (!age) {
			age = {'age':(key*10)+'-'+(key*10+9), 'frequency':0};
		}
		age.frequency += ageInfo[i].fields.num_cases; 
		if (key >= 0)
			ages[key] = age;
	}
	
	displayAge(error, ages);

	/* Gender pie chart */
	var widthGender = 250,
	heightGender = 220,
	radiusGender = Math.min(width, height) / 2;

	var color = d3.scale.ordinal()
	.range(["#FE7569", "#CDFFFF"]);

	var arc = d3.svg.arc()
	.outerRadius(radiusGender - 20)
	.innerRadius(radiusGender - 70);

	var pie = d3.layout.pie()
	.sort(null)
	.value(function(d) { return d.population; });

	var svgGender = d3.selectAll("#genderSplit").append("svg")
	.attr("width", widthGender)
	.attr("height", heightGender)
	.append("g")
	.attr("transform", "translate(" + widthGender / 2 + "," + heightGender / 2 + ")");

	var displayGender = function(error, data) {
		  data.forEach(function(d) {
		    d.population = +d.population;
		  });

		  var gData = svgGender.selectAll(".arc")
		      .data(pie(data));
		  var g =gData.enter().append("g")
		      .attr("class", "arc");
 
		  g.append("path")
		      .attr("d", arc)
		      .style("fill", function(d) { return color(d.data.gender); });

		  g.append("text")
		      .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
		      .attr("dy", ".35em")
		      .style("text-anchor", "middle")
		      .text(function(d) { return d.data.gender; });
		  
		  g.selectAll('path').each(function(d){
		  	var content = ' Cases Reported: ' + d.data.population;
       	 	$(this).popover({trigger:'hover', title:d.data.gender , placement:'top', content:content, container:"body"});
    	  });
		};


	
	displayGender(error, 
		[{'gender':'Male', 'population':gender[0].fields.male}, {'gender':'Female', 'population':gender[0].fields.female}]
	);

};
