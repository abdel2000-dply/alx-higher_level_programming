/*
  how to use the API provided by Stefan Bohacek:
  https://stefanbohacek.com/project/hellosalut-api/
*/

const url = 'https://hellosalut.stefanbohacek.dev/';

$(document).ready(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();

    $.getJSON(url, { lang: languageCode }, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });

  $('#language_code').keypress((ev) => {
    if (ev.which === 13) {
      $('#btn_translate').click();
    }
  });
});
