#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + parseInt(process.argv[2]);
let data;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    console.log(data.title);
  }
});
