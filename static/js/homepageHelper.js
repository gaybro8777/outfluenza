var assignBuckets = function(states) {
	var total = 0;
	var dict = {};
	for (var i = 0; i < states.length; i++) {
		dict[states[i].pk] = states[i];
		total += states[i].fields.num_cases;
	}
	dict['US'] = total;
	return dict;
}

var assignBucketsToZipcodes = function(zipcodes) {
	var dict = {}
	for (var i = 0; i < zipcodes.length; i++) {
		dict[zipcodes[i].pk] = zipcodes[i];
	}
	return dict;
}