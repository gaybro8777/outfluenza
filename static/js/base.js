var handleStateClick = function() {
	state = document.getElementById("stateSearch").value;
	if (state) {
		window.location.replace("/find/" + state);
	}
}

var handleZipcodeClick = function() {
	zipcode = document.getElementById("zipcodeSearch").value;
	if (zipcode) {
		window.location.replace("/find/" + zipcode);
	}
}