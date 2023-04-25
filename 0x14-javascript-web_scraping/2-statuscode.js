#!/usr/bin/node
// script that display the status code of a GET requeest
const request = require('request');
request
  .get(process.argv[2])
  .on('response', (response) => {
    console.log('code:', response.statusCode);
  });
