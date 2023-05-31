'use strict';
$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(`${url}/?format=json`, function (data, status) {
    data.results.forEach(film => {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});
