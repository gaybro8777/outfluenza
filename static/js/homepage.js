

queue()
    .defer(d3.json, "static/data/us_states_topo.json")
    .defer(d3.json, "/statesjson")
    .await(ready);

function ready(error, us, states) {
	updateMap(error, us, states);
	updateStatistics(error, us, us.objects.state.geometries);
}