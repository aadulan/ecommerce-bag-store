$(document).ready(function() {
    $('#bag-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        center: true,

        responsive: {
            0: {
                items: 1.5,
                nav: false,
                dots: false,
                slideBy: 1,

            },
            600: {
                items: 3,
                nav: true,
                slideBy: 2,
            },
            1000: {
                items: 5,
                nav: true,
                slideBy: 3,
            }
        }
    });


    $('.sub-brand-btn').click(function (event) {
        var bags_sub_brands = '.bag-card[sub-brand="' + event.target.id + '"]';
        var button = $('.sub-brand-btn#' + event.target.id);
        console.log(event.target.id);
        console.log($(bags_sub_brands));
        $(bags_sub_brands).toggle();
        button.toggleClass("active");

    })
     $('.brand-btn').click(function (event) {
        var bags_brands = '.bag-card[brand="' + event.target.id + '"]';
        var button = $('.brand-btn#' + event.target.id);
        console.log(event.target.id);
        console.log($(bags_brands));
        $(bags_brands).toggle();
        button.toggleClass("active");

    })
     $('.type-btn').click(function (event) {
        var bags_types = '.bag-card[type="' + event.target.id + '"]';
        var button = $('.type-btn#' + event.target.id);
        console.log(event.target.id);
        console.log($(bags_types));
        $(bags_types).toggle();
        button.toggleClass("active");

    })


});
