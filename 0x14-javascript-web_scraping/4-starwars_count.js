#!/usr/bin/node
// Script that prints the number of movies a character was present
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, function (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    const count = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count;
    }, 0);
    console.log(count);
  }
});
