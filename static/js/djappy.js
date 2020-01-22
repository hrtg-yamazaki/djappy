$(function(){

  // **** PC表示のメニュー展開 **** //
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


  // **** タブレット・スマートフォンのメニュー展開 **** //
  
  $(".header-sp-menu").click(function(){

    $(".hidden-menu").slideToggle();

  })

  $(".hidden-close-sp__button").click(function(){

    $(".hidden-menu").slideToggle();

  })


  // **** device-width 変動時の表示調整 **** //

  $(window).resize(function(){

    var windowWidth = $(window).width();
    if (windowWidth <= 700){
      $('.header-menu').css('display', 'none');
    } else {
      $('.header-menu').css('display', 'inline');
    }

  })
   

})

