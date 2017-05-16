(function() {
	'use strict';

	function resize() {
		var width = document.body.clientWidth + "px";
		resize.triangle.style.borderRight = "solid " + width + " white";
	}
	resize.triangle = document.getElementById("tri-bottom");
	
	resize();
	addEventListener("resize", resize);
})();
