(function() {
    'use strict';

    var nav = document.getElementsByTagName("nav")[0];
    var scrolled = false;

    function onScroll() {
        var sTop = document.body.scrollTop;
        
        if (sTop > 0 && !scrolled) {
            nav.setAttribute("class", "scrolled");
            scrolled = true;
        } else if (sTop <= 0 && scrolled) {
            nav.setAttribute("class", "");
            scrolled = false;
        }
    }

    var triLeft = document.getElementsByClassName("tri-left")[0];
    var triRight = document.getElementsByClassName("tri-right")[0];
    
    function resizeTriangles() {
        var width = document.body.clientWidth;
        var height = document.body.clientHeight;
        
        var triWidth = Math.floor(width / 2) + "px";
        triLeft.style.borderRightWidth = triWidth;
        triRight.style.borderLeftWidth = triWidth;
    }

    addEventListener("scroll", onScroll);
    resizeTriangles();
    addEventListener("resize", resizeTriangles);

    // Utility methods
    String.prototype.capitalize = function() {
        return this.charAt(0).toUpperCase() + this.slice(1);
    }
})();
