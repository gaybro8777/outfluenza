
var $statemap = $('#interactiveMap');
var state = $statemap.data('root')

queue()
    .defer(d3.json, "/static/data/" + state + ".json")
    .defer(d3.json, "/zipcodesjson/" + state)
    .await(ready);

function ready(error, stateJson, zipcodes) {
    $statemap.updateMap(error, stateJson, zipcodes);
}