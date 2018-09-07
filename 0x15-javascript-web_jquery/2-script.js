// This script will turn red when clicked.
// This is a javascript script that will update the text color of the HEADER
// HTML to red (#FF0000) when a user clicks on the tag 'DIV#red_header'
$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
