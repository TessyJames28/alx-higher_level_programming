$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;

    // Make the API request
    $.get(url, function (data) {
      const helloMsg = data.hello;
      $('#hello').text(helloMsg);
    });
  });
});
