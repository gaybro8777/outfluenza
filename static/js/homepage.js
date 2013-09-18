

queue()
    .defer(d3.json, "/static/data/us_states_topo.json")
    .defer(d3.json, "/statesjson")
    .defer(d3.json, "/ustimegraphjson")
    .await(ready);

function ready(error, us, states, stateStatistics) {
	updateMap(error, us, states);
	updateStatistics(error, stateStatistics);
}