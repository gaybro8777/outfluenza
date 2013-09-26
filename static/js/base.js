var handleStateClick = function() {
	state = document.getElementById("stateSearch").value;
	if (state) {
		window.location.replace("/findState/" + state);
	}
}

var handleZipcodeClick = function() {
	zipcode = document.getElementById("zipcodeSearch").value;
	if (zipcode) {
		console.log("here")
		window.location.replace("/findZipcode/" + zipcode);
	}
}