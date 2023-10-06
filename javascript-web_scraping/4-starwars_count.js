#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

const characterId = 18;
request(URL, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const filmData = JSON.parse(body);
  let count = 0;

  filmData.results.forEach((film) => {
    film.characters.forEach((characterURL) {
      if (characterURL.includes('people/' + characterId)) {
      count++;
      return;
      }
    });
  });
  console.log(count);
});
