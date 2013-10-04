
var $statemap = $('#interactiveMap');
var state = $statemap.data('root')

queue()
    .defer(d3.json, "/static/data/" + state + ".json")
    .defer(d3.json, "/countyjson/" + state)
    .defer(d3.json, "/genderjson/" + state)
    .defer(d3.json, "/agejson/" + state)
    .defer(d3.json, "/statetimegraphjson/" + state)
    .defer(d3.json, "/topmetrics/" + state)
    .await(ready);

function ready(error, stateJson, counties, genderInfo, ageInfo, timeMessages, metrics) {
    $statemap.updateMap(error, stateJson, counties);
    updateGenderAndAge(error, genderInfo, ageInfo);
    updateTimeChart(timeMessages);
    topMetrics(metrics[0].fields)
}

var topMetrics = function(data) {
	document.getElementById("worstZipcode").innerHTML=data.worstZipcode;
	document.getElementById("numRecentCases").innerHTML=data.numRecentCases + ' new cases';
	document.getElementById("percentIncrease").innerHTML=data.percentIncrease + '%';
};