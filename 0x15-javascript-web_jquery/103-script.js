$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    $.get(url + languageCode, (data) => {
      const helloMsg = data.hello;
      $('#hello').text(helloMsg);
    });
  });

  $('#language_code').keydown((event) => {
    if (event.keyCode === 13) {
      const languageCode = $('#language_code').val();
      $.get(url + languageCode, (data) => {
        $('#hello').text(data.hello);
      });
    }
  });
});
