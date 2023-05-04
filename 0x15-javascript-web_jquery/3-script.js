// JavaScript script that adds the class red to the <header> element when
// the user clicks on the tag DIV#red_header
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').addClass('red');
  });
});
