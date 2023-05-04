// JavaScript script that toggles the class of the <header> element to green
// or red when the user clicks on the tag DIV#toggle_header
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').toggleClass('red green');
  });
});
