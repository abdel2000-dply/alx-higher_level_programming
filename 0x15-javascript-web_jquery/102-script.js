/*
  how to use the API provided by Stefan Bohacek:
  https://stefanbohacek.com/project/hellosalut-api/
*/
const url = 'https://hellosalut.stefanbohacek.dev/';
$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const language = $('INPUT#language_code').val();
    $.get(url, { lang: language }, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
