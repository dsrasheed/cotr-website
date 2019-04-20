(function() {
    'use strict';

    /* NAVIGATION */
    var nav = document.getElementsByTagName("nav")[0];

    // onScroll navigation animation
    var scrolled = false;
    addEventListener("scroll", () => {
        if (window.scrollY > 0 && !scrolled) {
            nav.setAttribute("class", "scrolled");
            scrolled = true;
        } else if (window.scrollY <= 0 && scrolled) {
            nav.setAttribute("class", "");
            scrolled = false;
        }
    });

    // mobile navigation animations
    var hamburger = nav.querySelector('.hamburger');
    var mobileNav = document.querySelector('aside.mobile-nav');
    var clicked = false;
    hamburger.addEventListener('click', () => {
        if (!clicked) {
            hamburger.classList.add('clicked');
            mobileNav.classList.add('display');
        }
        else {
            hamburger.classList.remove('clicked');
            mobileNav.classList.remove('display');
        }
        clicked = !clicked;
    });


    /* UI ELEMENTS */
    var triLeft = document.getElementsByClassName("tri-left")[0];
    var triRight = document.getElementsByClassName("tri-right")[0];
    
    function resizeTriangles() {
        var width = document.body.clientWidth;
        var height = document.body.clientHeight;
        
        var triWidth = Math.floor(width / 2) + "px";
        triLeft.style.borderRightWidth = triWidth;
        triRight.style.borderLeftWidth = triWidth;
    }

    resizeTriangles();
    addEventListener("resize", resizeTriangles);

    /* UTILITY */
    String.prototype.capitalize = function() {
        return this.charAt(0).toUpperCase() + this.slice(1);
    }
})();
