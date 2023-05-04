// JavaScript script that adds, removes and clears LI elements
// from a list when the user clicks
$('document').ready(() => {
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(() => {
    $('.my_list li:last-child').remove();
  });
  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});
