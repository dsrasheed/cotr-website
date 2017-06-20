(function() {
    'use strict';

    var schedule = document.getElementsByClassName('schedule-slide')[0];
    function scheduleResized() {
        var scheduleWidth = this.clientWidth;
        if (scheduleWidth >= 500)
            this.classList.add('no-responsive');
        else {
            if (this.classList.contains('no-responsive'))
                this.classList.remove('no-responsive');
        }
    };
    addEventListener('resize', scheduleResized.bind(schedule));
    scheduleResized.call(schedule);
    
    // A module to control the animation of the slide widget
    function Slide() {
        var timeSlides = [];
        var infoSlides = [];

        function createSlides(slideList, className, containerClass) {
            var container = document.getElementsByClassName(containerClass)[0];
            for (var i = -1; i <= 1; i++) {
                let slide = document.createElement('div');
                slide.className = className;
                slide.style.left = i * 100 + '%';

                slideList.push(slide);
                container.appendChild(slide);
            }
        }

        function createTimeSlides() {
            createSlides(timeSlides, 'schedule-time',
                        'schedule-time-container');
        }

        function createInfoSlides() {
            createSlides(infoSlides, 'schedule-time-info',
                        'schedule-time-info-container');
        }

        function getFormattedTime(hours, minutes) {
            return hours + ":" + (minutes < 10  ? "0" + minutes : minutes);
        }

        function animateSlides(slideList, newContent, animDirection) {
            var leftSlide  = slideList[0];
            var midSlide   = slideList[1];
            var rightSlide = slideList[2];
        
            var updatedSlideList = [];
            if (animDirection === 'right') {
                rightSlide.innerHTML = newContent;
                
                // Don't want slides to slide on top of each other.
                leftSlide.style.zIndex = '0';
                midSlide.style.zIndex = '1';
                rightSlide.style.zIndex = '1';
              
                // Animated sliding effect with a transition on left.
                midSlide.style.left = '-100%';
                rightSlide.style.left = '0';
                leftSlide.style.left = '100%';

                updatedSlideList.push(midSlide);
                updatedSlideList.push(rightSlide);
                updatedSlideList.push(leftSlide);
            } else {
                leftSlide.innerHTML = newContent;

                leftSlide.style.zIndex = '1';
                midSlide.style.zIndex = '1';
                rightSlide.style.zIndex = '0';

                rightSlide.style.left = '-100%';
                midSlide.style.left = '100%';
                leftSlide.style.left = '0';

                updatedSlideList.push(rightSlide);
                updatedSlideList.push(leftSlide);
                updatedSlideList.push(midSlide);
            }

            updatedSlideList.forEach(function(s, index) { 
                slideList[index] = s; 
            });
        }

        function animate(animDirection) {
            animateSlides(timeSlides, this.timeText, animDirection);
            animateSlides(infoSlides, this.info, animDirection);
        }

        createTimeSlides();
        createInfoSlides();        
        return {
            getFormattedTime: getFormattedTime,
            timeText: "",
            info: "",
            animate: animate
        };
    }
    
    // A module to control the animation of the clock widget.
    function Clock(hourHand, minuteHand) {
        // In degrees per second
        const hHandRotateRate = 30;
        const mHandRotateRate = 360;

        // TODO: Should find the position of the hands when 
        // function is called rather than set to 0.
        var currentHour = 0;
        var currentMinute = 0;
        var hCurrentRotation = 0;
        var mCurrentRotation = 0;

        function getClockChangeDegrees(start, end) {
            var change = end - start;
            return (change / 12) * 360;
        }

        function getHourChangeDegrees(mStart, mEnd, hStart, hEnd) {
            var hDegrees = getClockChangeDegrees(hStart, hEnd);
            hDegrees += ((mEnd - mStart) / 60) * 30;
            return hDegrees;
        }

        function getMinuteChangeDegrees(mStart, mEnd, hStart, hEnd) {
            // Make full rotations for the difference in hours
            var hDegrees = (hEnd - hStart) * 360;
            
            // Get degree change for difference in minutes
            var mDegrees = getClockChangeDegrees(mStart / 5, mEnd / 5);
            return hDegrees + mDegrees;
        }

        function animate() {
            var hHandDegrees = getHourChangeDegrees(currentMinute, this.minute,
                                                    currentHour, this.hour);
            var mHandDegrees = getMinuteChangeDegrees(currentMinute, this.minute,
                                                    currentHour, this.hour);
            currentHour = this.hour;
            currentMinute = this.minute;

            var hDuration = (hHandDegrees / hHandRotateRate) + 's';
            var mDuration = (mHandDegrees / mHandRotateRate) + 's';
            hourHand.style.transitionDuration = hDuration;
            minuteHand.style.transitionDuration = mDuration;

            hCurrentRotation += hHandDegrees;
            mCurrentRotation += mHandDegrees;
            hourHand.style.transform = 'rotate(' + hCurrentRotation + 'deg)';
            minuteHand.style.transform = 'rotate(' + mCurrentRotation + 'deg)';
        }

        return {
            hour: 0,
            minute: 0,
            animate: animate
        };
    }

    // Get the buttons used to interact with the slide.
    var leftButtons = document.getElementsByClassName('left-angle');
    var rightButtons = document.getElementsByClassName('right-angle');

    // Convert HTMLCollection to array so it can be iterated over.
    leftButtons = [].slice.call(leftButtons);
    rightButtons = [].slice.call(rightButtons);
    var buttons = leftButtons.concat(rightButtons);
    
    buttons.forEach(function(button) {
        var direction = button.classList.contains('left-angle') ? 'left' : 'right';
        button.direction = direction;
        button.addEventListener('click', slideButtonClicked);
    });
    
    // Data to display on schedule
    var scheduleData = document.getElementById('schedule-data').attributes;
    scheduleData = [].slice.call(scheduleData);
    scheduleData = scheduleData.slice(2); // Keep all attributes except id and style

    // Used to index an attribute on scheduleData
    var dataIndex = -1;

    // Widgets
    var hourHand = document.getElementsByClassName('hour-hand')[0];
    var minuteHand = document.getElementsByClassName('minute-hand')[0];
    var clock = Clock(hourHand, minuteHand);
    var slide = Slide();

    // When a user clicks on the buttons on the schedule slide, this
    // updates the time and info associated with the time.
    function slideButtonClicked() {
        var leftDirection = this.direction === 'left';
        dataIndex += leftDirection ? -1 : 1;
        if (dataIndex < 0)
            dataIndex = scheduleData.length - 1;
        else if (dataIndex >= scheduleData.length)
            dataIndex = 0;
        
        // Take 'time00:00' -> [number 00, number 00]
        function parseTime(timeText) {
            var time = timeText.substring('time'.length);
            var timeElems = time.split(':');
            return [Number(timeElems[0]), Number(timeElems[1])];
        }

        var data = scheduleData[dataIndex];
        var time = parseTime(data.nodeName);
        var info = data.nodeValue;

        clock.hour = time[0];
        clock.minute = time[1];
        slide.timeText = slide.getFormattedTime(time[0], time[1]);
        slide.info = info;

        clock.animate();
        slide.animate(this.direction);
    }

    buttons[2].click();
})();
