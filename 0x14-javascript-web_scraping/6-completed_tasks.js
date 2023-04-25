#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const todos = JSON.parse(body);
    for (const todo in todos) {
      const task = todos[todo];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('Error code:', response.statusCode);
  }
});
