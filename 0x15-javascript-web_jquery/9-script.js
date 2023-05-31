$(function () {
  const url = 'https://fourtonfish.com';

  $.get(`${url}/hellosalut/?lang=fr`, function (data, status) {
    $('DIV#hello').html(data.hello);
  });
});
