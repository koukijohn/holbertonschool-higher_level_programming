#!/usr/bin/node
// This script will made the header toggle from green to red.
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
