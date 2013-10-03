
var $statemap = $('#interactiveMap');
var state = $statemap.data('root')

queue()
    .defer(d3.json, "/static/data/" + state + ".json")
    .defer(d3.json, "/countyjson/" + state)
    .defer(d3.json, "/genderjson/" + state)
    .defer(d3.json, "/agejson/" + state)
    .defer(d3.json, "/statetimegraphjson/" + state)
    .await(ready);

function ready(error, stateJson, counties, genderInfo, ageInfo, timeMessages) {
    $statemap.updateMap(error, stateJson, counties);
    updateGenderAndAge(error, genderInfo, ageInfo);
    updateTimeChart(timeMessages);
}