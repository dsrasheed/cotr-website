(function() {
	'use strict';

	var nav = document.getElementsByTagName("nav")[0];
	var scrolled = false;

	function onScroll() {
		var sTop = document.body.scrollTop;
		console.log("SCROLL TOP " + sTop);
		if (sTop > 0 && !scrolled) {
			nav.style.height = "80px";
			nav.style.backgroundColor = "white";
			nav.style.color = "black";
			nav.style.borderBottom = "none";

			scrolled = true;
		} else if (sTop <= 0 && scrolled) {
			nav.style.height = "130px";
			nav.style.backgroundColor = "transparent";
			nav.style.color = "white";
			nav.style.borderBottom = "solid 1px rgba(255,255,255,0.6)";

			scrolled = false;
		}
	}

	addEventListener("scroll", onScroll);
})();
