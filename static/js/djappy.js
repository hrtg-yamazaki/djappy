$(function(){


  $(".header-menu").click(function(){

    $(this).next(".header-links").slideToggle();
    $(this).css("display", "none");
    $(".header-close").css("display", "inline");
  
  });

  $(".header-close").click(function(){

    $(".header-links").slideToggle();
    $(this).css("display", "none");
    $(".header-menu").css("display", "inline");

  })


  $(".header-sp-menu").click(function(){
    $(".hidden-menu").slideToggle();
  })

  $(".hidden-close-sp__button").click(function(){
    $(".hidden-menu").slideToggle();
  })

})

