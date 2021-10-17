jQuery(document).ready(function(){
"use strict";


/* =============== Sticky Header ===================== */
$(window).scroll(function() {    
    var scroll = $(window).scrollTop();
    if (scroll >= 70) {
        $("header").addClass("sticky");
    }
    else{
        $("header").removeClass("sticky");
    }
}); 


/*=================== Responsive Header ===================*/  
$(".responsive-header > span").click(function(){
    $(this).next('ul').slideToggle();
    $(".responsive-header > ul > li > ul").slideUp();
    $(".responsive-header > ul > li > ul > li > ul").slideUp();
    $(".responsive-header > ul > li").removeClass('opened');
    $(".responsive-header > ul > li > ul > li").removeClass('opened');
}); 

$('.responsive-header ul li a').next('ul').parent().addClass('no-link')
$('.no-link > a').click(function(){
    return false;
}); 


$(".responsive-header > ul > li > a").click(function(){
    $(".responsive-header > ul > li > ul").slideUp();
    $(".responsive-header > ul > li").removeClass('opened');
    $(this).next('ul').slideDown();
    $(this).next('ul').parent().toggleClass('opened');
}); 
$(".responsive-header > ul > li > ul > li a").click(function(){
    $(".responsive-header > ul > li > ul > li > ul").slideUp();
    $(".responsive-header > ul > li > ul > li").removeClass('opened');
    $(this).next('ul').slideDown();
    $(this).next('ul').parent().toggleClass('opened');
}); 
    


/* =============== Ajax Contact Form ===================== */
$('#contactform').submit(function(){
    var action = $(this).attr('action');
    $("#message").slideUp(750,function() {
    $('#message').hide();
        $('#submit')
        .after('<img src="images/ajax-loader.gif" class="loader" />')
        .attr('disabled','disabled');
    $.post(action, {
        name: $('#name').val(),
        email: $('#email').val(),
        txtsubject: $('#txtsubject').val(),
        page: $('#page').val(),
        comments: $('#comments').val(),
        verify: $('#verify').val()
    },
        function(data){
            document.getElementById('message').innerHTML = data;
            $('#message').slideDown('slow');
            $('#contactform img.loader').fadeOut('slow',function(){$(this).remove()});
            $('#submit').removeAttr('disabled');
            if(data.match('success') != null) $('#contactform').slideUp('slow');

        }
    );
    });
    return false;
});


/* =============== Testimonial Selectors ===================== */
$(".client-img").click(function(){
  $(".client-img").removeClass("active");
  $(this).addClass("active");
});


/* =============== Kenburns Text Centralization ===================== */
var kenburnstext = $('.kenburns-text').height();
var textmargin = kenburnstext/2;
jQuery('.kenburns-text').css({
  "margin-top":-textmargin
});



});


$(window).load(function(){
/* =============== Page Loader ===================== */
  $(".page-loader").fadeOut(3000);


/* =============== Text Carousel Centralization ===================== */
var textcarousel = $('.text-carousel').height();
var carouselmargin = textcarousel/2;
jQuery('.text-carousel').css({
  "margin-top":-carouselmargin
});

/* =============== Pretty Photo ===================== */
  jQuery("body a[data-rel^='prettyPhoto']").prettyPhoto({
      theme: "facebook",
  });
});






