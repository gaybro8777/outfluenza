var assignBuckets = function(states) {
	var dict = {};
	for (var i = 0; i < states.length; i++) {
		dict[states[i].pk] = states[i];
	}
	return dict;
}

var assignBucketsToZipcodes = function(zipcodes) {
	var dict = {}
	for (var i = 0; i < zipcodes.length; i++) {
		dict[zipcodes[i].pk] = zipcodes[i];
	}
	return dict;
}