//When the website is loaded
$(document).ready(function() {
  document.getElementById("quote_text").focus();
  // $('thought').hide();
  // var eT = 0;
  // $('.thought').hide().each(function() {
  //     $(this).delay(eT).fadeIn('slow');
  //     eT += 200;
  // });
  $('.thought').click(function(){
    $(this).toggleClass('extend');
  });

  $('.thought:first-child').addClass('extend');
});
