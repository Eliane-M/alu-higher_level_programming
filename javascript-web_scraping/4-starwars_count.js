#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api/films/';

const characterId = 18;
request(URL, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const filmData = JSON.parse(body);
  let count = 0;

  filmData.results.forEach((film) => {
    if (film.characters.includes(URL, 'people/', characterId)) {
	count++;
	return;
    }
    console.log(count);
  });
});
