

queue()
    .defer(d3.json, "/static/data/us_states_topo.json")
    .defer(d3.json, "/statesjson")
    .defer(d3.json, "/ustimegraphjson")
    .defer(d3.json, "/topzipcodesjson")
    .await(ready);

function ready(error, us, states, stateStatistics, topZipcodes) {
    updateTopStateStats(error, states);
	 updateTopZipcodeStats(error, topZipcodes);
	
	var $usmap = $('#interactiveMap');
    $usmap.updateMap(error, us, states);
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