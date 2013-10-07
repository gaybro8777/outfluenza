var globalUS;

queue()
    .defer(d3.json, "/static/data/us_states_topo.json")
    .defer(d3.json, "/statesjson")
    .defer(d3.json, "/ustimegraphjson")
    .defer(d3.json, "/topzipcodesjson")
    .await(ready);

function ready(error, us, states, stateStatistics, topZipcodes) {
  updateTopStateStats(error, states);
	updateTopZipcodeStats(error, topZipcodes);
	globalUS = us;
	updateMap(error, us, states);
	//updateStatistics(error, stateStatistics);
}

/* Time lapse slider */
$(function() {
    $( "#slider" ).slider({
      value: 7,
      min: 0,
      max: 14,
      step: 1,
      slide: function( event, ui ) {
        $( "#amount" ).val( ui.value );
      }
    });
    $( "#amount" ).val( $( "#slider" ).slider( "value" ) );
});

/* Accordion stats */
$(function() {
    $( "#accordion" ).accordion({
      heightStyle: "content"
    });
});

$(function() {
    $( "#accordion2" ).accordion({
      heightStyle: "content"
    });
});

var handleZipcodeClick = function(){
  var data = [["name1", "city1", "some other info"], ["name2", "city2", "more info"]];
  var csvContent = "data:text/csv;charset=utf-8,";
  data.forEach(function(infoArray, index){
    dataString = infoArray.join(",");
    csvContent += index < infoArray.length ? dataString+ "\n" : dataString;
  }); 
  var encodedUri = encodeURI(csvContent);
  window.open(encodedUri);
}

var predictMap = function(num) {
  d3.json('/statesjsonprediction/'+num, function(states) {
    var bucketDict = assignBuckets(states);
    d3.select("#interactiveMap").selectAll('path').each(function(d) {
      var bucket = bucketDict[d.properties.STUSPS10];
      var stateClass = "q" + (bucket ? bucket.fields.bucket : d3.select(this).attr('class')) + "-9"; 
      d3.select(this).attr('class', stateClass);
    });
  });
}