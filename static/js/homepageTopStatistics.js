var updateTopStateStats = function(error, states) {
		var index = 0;
		var iterVal = function() {
			index++;
			return index+'.';
		}
		var data_states = states;
		data_states = states.slice(0, 3);

		var width = 250,
	    	height = 100,
	    	margin = {top: 10, right: 10, bottom: 10, left: 10};

	    var table = d3.select("#topStatesTable").append("table")
			.attr("width", width)
			.attr("height", height)
			.attr('class', 'table-corner')
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")")
			
		table.append('thead').append('tr')
				.style('background-color', function(d,i) {
					return i%2 ? '#fbfbfb' : '#fdfdfd';
				})
				.selectAll('th')
				.data(["", "State", "# Patients"])
				.enter()
				.append('th')
				.text(function(d) { return d})
				.attr('class', 'table-rank stateHeader');

		var rows = table.append('tbody').selectAll('tr')
			.data(data_states)
			.enter()
			.append('tr')
			.style('background-color', function(d,i) {
				return i%2 ? '#fbfbfb' : '#fdfdfd';
			});

		rows.selectAll('td')
			.data(function(row) {
				return [iterVal(), row.pk, row.fields.num_female_cases + row.fields.num_male_cases]
			})
			.enter()
			.append('td')
			.attr('class', 'tableData stateBody')
			.text(function(d) { return d});

	};

var updateTopZipcodeStats = function(error, zipcodes) {
		var index = 0;
		var iterVal = function() {
			index++;
			return index+'.';
		}
		var width = 280,
	    	height = 100,
	    	margin = {top: 10, right: 10, bottom: 10, left: 10};

	    var table = d3.select("#topZipcodesTable")
			.attr("width", width)
			.attr("height", height)
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")")
			.append("table")
			.attr('class', 'table-corner')
			.style('align', 'center')
			.append('tbody');
		
		table.append('thead').append('tr')
				.style('background-color', function(d,i) {
					return i%2 ? '#fbfbfb' : '#fdfdfd';
				})
				.selectAll('th')
				.data(["","Zip Code", "State Zip is in", "Number of Influenza Patients"])
				.enter()
				.append('th')
				.attr('class', 'table-company zipHeader')
				.text(function(d) { return d; });

		var rows_states = table.append('tbody').selectAll('tr')
			.data(zipcodes)
			.enter()
			.append('tr')
			.style('background-color', function(d,i) {
				return i%2 ? '#fbfbfb' : '#fdfdfd';
			});

		rows_states.selectAll('td')
			.data(function(row) {
				return [iterVal(), row.pk, row.fields.state, row.fields.malePatientCases + row.fields.femalePatientCases]
			})
			.enter()
			.append('td')
			.attr('class', 'tableData zipBody')
			.text(function(d) { return d});
	};