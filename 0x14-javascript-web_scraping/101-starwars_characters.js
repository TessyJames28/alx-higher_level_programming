#!/usr/bin/node
// script that prints all characters of a Star War movie
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
request.get(apiUrl + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const artists = JSON.parse(body).characters;
  displayArtists(artists, 0);
});

function displayArtists (artists, index) {
  request.get(artists[index], function (err, response, body) {
    if (!err) {
      const jsonResp = JSON.parse(body);
      console.log(jsonResp.name);
      if (index + 1 < artists.length) {
        displayArtists(artists, index + 1);
      }
    }
  });
}
