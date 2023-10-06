#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('provide URL');
  process.exit(1);
}

const apiURL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(apiURL, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: Received code', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  console.log(movieData.title);
});
