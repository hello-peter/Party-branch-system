jQuery(document).ready(function($){
    
    // Bootstrap menu fix
    $(".navbar-toggle").click(function(){
        $(".header").css('background', '#000');
    });
    
    
    $(".navbar-nav li a").click(function(){
        $(".navbar-collapse").removeClass('in');
    });
    
    
    // Scrolly parallax
    $('.overlay-bg').scrolly({bgParallax: true});
    
    // jQuery sticky menu
    $(".header").sticky({topSpacing:0});

    // jQuery smooth scroll
    $('.navbar-nav li a, .scroll-to-bottom a').bind('click', function(event) {
        var $anchor = $(this);
        var headerH = $('.header').outerHeight();
        $('html, body').stop().animate({
            scrollTop : $($anchor.attr('href')).offset().top - headerH + "px"
        }, 1200, 'easeInOutExpo');

        event.preventDefault();
    });    
    
    // jQuery scroll psy
    $('body').scrollspy({ 
        target: '.navbar-collapse',
        offset: 95
    })    

    // Owl Carousel
    $('.client-list').owlCarousel({
        loop:true,
        margin:10,
        responsiveClass:true,
        autoplay: 5000,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:4
            }
        }
    })
    
    
});


// jQuery type effect

var TxtType = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 1000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
};

TxtType.prototype.tick = function() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];

    if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

    var that = this;
    var delta = 150 - Math.random() * 100;

    if (this.isDeleting) { delta /= 2; }

    if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.loopNum++;
    delta = 500;
    }

    setTimeout(function() {
    that.tick();
    }, delta);
};

window.onload = function() {
    var elements = document.getElementsByClassName('typewrite');
    for (var i=0; i<elements.length; i++) {
        var toRotate = elements[i].getAttribute('data-type');
        var period = elements[i].getAttribute('data-period');
        if (toRotate) {
          new TxtType(elements[i], JSON.parse(toRotate), period);
        }
    }
    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".typewrite > .wrap { border-right: 0.02em solid #fff}";
    document.body.appendChild(css);
};  