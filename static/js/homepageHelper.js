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
	var total = 0;
	var dict = {};
	for (var i = 0; i < counties.length; i++) {
		dict[counties[i].pk] = counties[i];
		counties[i].fields.num_cases = counties[i].fields.num_male_cases + counties[i].fields.num_female_cases
		total += counties[i].fields.num_cases;
	}
	dict['STATE'] = total;
	return dict;
}

var firstKey = function(obj) {
    for (var a in obj) return a;
}

var assignPaths = function(us) {
	var dict = {};
	for (var i = 0; i < us.length; i++) {
		dict[us[i].properties.NAME10.toUpperCase()] = us[i];
		dict[us[i].properties.STUSPS10.toUpperCase()] = us[i];
	}
	return dict;
}