#!/usr/bin/node
// script that prints all characters of a Star War movie
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
request.get(apiUrl + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const values = JSON.parse(body);
  const character = values.characters;
  for (const idx of character) {
    request.get(idx, function (err, response, nbody) {
      if (err) {
        console.error(err);
      }
      const artists = JSON.parse(nbody);
      console.log(artists.name);
    });
  }
});
