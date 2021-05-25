$(document).ready(function() {
  $('.toggle').click(function() {
    var current_status = $('.status').text();
    if (current_status === 'Untoggled'){
      $('.status').html('Toggled');
    } else {
      $('.status').html('Untoggled');
    }
  });
});
