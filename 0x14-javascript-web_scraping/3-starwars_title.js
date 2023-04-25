#!/usr/bin/node
// script that prints the title of a Star Wars movie based on number of episode
const request = require('request');
const episode = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
request(apiUrl + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonResp = JSON.parse(body);
    console.log(jsonResp.title);
  } else {
    console.log('Error Code:', response.statusCode);
  }
});
