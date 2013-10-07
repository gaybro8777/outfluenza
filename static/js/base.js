var handleStateClick = function() {
	state = document.getElementById("stateSearch").value;
	if (state) {
		window.location.replace("/find/" + state);
	}
}

var handleZipcodeClick2 = function() {
	zipcode = document.getElementById("zipSearchBox").value;
	if (zipcode) {
		window.location.replace("/find/" + zipcode);
	}
}