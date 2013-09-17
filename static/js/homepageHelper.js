var assignBuckets = function(us, states) {
	var dict = {};
	for (var i = 0; i < states.length; i++) {
		dict[states[i].pk] = states[i];
	}
	return dict;
}
