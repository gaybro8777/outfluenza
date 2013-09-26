

queue()
    .defer(d3.json, "/static/data/us_geo.json")
    .defer(d3.json, "/messagesjson")
    //.defer(d3.json, "/ustimegraphjson")
    .await(ready);


function ready(error, us, messages) {
	var $usmap = $('#interactiveMap');
    $usmap.updateMap(error, us, messages);
	//updateStatistics(error, stateStatistics);
	//updateTopStats(stateStatistics);
}