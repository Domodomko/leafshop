function readMore() {
    document.getElementById('about_tea_text_short').style.display = "none";
    document.getElementById('about_tea_read_more').style.display = "none";
    document.getElementById('about_tea_text_full').style.display = "block";
}

$(function() {

    var introH = $("#intro").innerHeight(),
        header = $("#header"),
        scrollOffset = $(window).scrollTop(),
        navlink = document.getElementsByClassName("nav__link"),
        nav_check = false,
        scrolltop= $("#scrolltop");


//  Smooth Scroll

    $("[data-scroll]").on("click", function(event) {
        event.preventDefault();
        nav_check=true
        var $this = $(this),
            blockId = $(this).data('scroll'),
            blockOffset = $(blockId).offset().top - 150;

        $("html, body").animate({
            scrollTop: blockOffset
        }, 500);
        nav_check=false;
    });

    $("#nav_toggle").on("click", function(event) {
        event.preventDefault();

        $(this).toggleClass("active");
        $("#nav").toggleClass("active");
    });

    $('#categories').on('change', function() {
      $('[data-category]').hide();
      $(`[data-category=${this.value}]`).show();
    });
});
