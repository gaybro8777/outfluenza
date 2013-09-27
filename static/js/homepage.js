

queue()
    .defer(d3.json, "/static/data/us_states_topo.json")
    .defer(d3.json, "/statesjson")
    .defer(d3.json, "/ustimegraphjson")
    .defer(d3.json, "/topzipcodesjson")
    .await(ready);

function ready(error, us, states, stateStatistics, topZipcodes) {
    var $topStatesTable = $('#topStatesTable');
    $topStatesTable.updateTopStateStats(error, states);

    var $topZipcodesTable = $('#topZipcodesTable');
	$topZipcodesTable.updateTopZipcodeStats(error, topZipcodes);
	
	var $usmap = $('#interactiveMap');
    $usmap.updateMap(error, us, states);
	updateStatistics(error, stateStatistics);
}