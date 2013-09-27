(function($){
	$.fn.updateTopStateStats = function(error, states) {

		var data_states = states;
		if (states.length > 3) {
			data_states = states.slice(0, 3);
		}

		var width = 250,
	    	height = 100,
	    	margin = {top: 10, right: 10, bottom: 10, left: 10};

	    var table = d3.select("#topStatesTable").append("table")
			.attr("width", width)
			.attr("height", height)
			.attr('class', 'table table-hover')
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")")
			
		table.append('thead').append('tr')
				.style('background-color', function(d,i) {
					return i%2 ? '#fbfbfb' : '#fdfdfd';
				})
				.selectAll('td')
				.data(["State", "# Patients"])
				.enter()
				.append('td')
				.text(function(d) { return d})
				.style('text-align', 'center')
				.style('font-weight', 'bold');

		var rows = table.append('tbody').selectAll('tr')
			.data(data_states)
			.enter()
			.append('tr')
			.style('background-color', function(d,i) {
				return i%2 ? '#fbfbfb' : '#fdfdfd';
			});

		rows.selectAll('td')
			.data(function(row) {
				return [row.pk, row.fields.num_cases]
			})
			.enter()
			.append('td')
			.style('text-align', 'center')
			.text(function(d) { return d});

	};

	$.fn.updateTopZipcodeStats = function(error, zipcodes) {
		var width = 280,
	    	height = 100,
	    	margin = {top: 10, right: 10, bottom: 10, left: 10};

	    var table = d3.select("#topZipcodesTable")
			.attr("width", width)
			.attr("height", height)
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")")
			.append("table")
			.attr('class', 'table table-hover')
			.style('align', 'center')
			.append('tbody');
		
		table.append('thead').append('tr')
				.style('background-color', function(d,i) {
					return i%2 ? '#fbfbfb' : '#fdfdfd';
				})
				.selectAll('td')
				.data(["Zipcode", "State", "# Patients"])
				.enter()
				.append('td')
				.text(function(d) { return d})
				.style('text-align', 'center')
				.style('font-weight', 'bold');

		var rows_states = table.append('tbody').selectAll('tr')
			.data(zipcodes)
			.enter()
			.append('tr')
			.style('background-color', function(d,i) {
				return i%2 ? '#fbfbfb' : '#fdfdfd';
			});

		rows_states.selectAll('td')
			.data(function(row) {
				return [row.pk, row.fields.state, row.fields.patientCases]
			})
			.enter()
			.append('td')
			.style('text-align', 'center')
			.text(function(d) { return d});
	};
})(jQuery);