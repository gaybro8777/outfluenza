var assignBuckets = function(states) {
	var total = 0;
	var dict = {};
	for (var i = 0; i < states.length; i++) {
		dict[states[i].pk] = states[i];
		states[i].fields.num_cases = states[i].fields.num_male_cases + states[i].fields.num_female_cases
		total += states[i].fields.num_cases;
	}
	dict['US'] = total;
	return dict;
}

var assignBucketsToCounties = function(counties) {
	var dict = {}
	for (var i = 0; i < counties.length; i++) {
		dict[counties[i].pk] = counties[i];
	}
	return dict;
}

var firstKey = function(obj) {
    for (var a in obj) return a;
}