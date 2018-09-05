#!/usr/bin/node
// This is a script that computes the number of tasks completed by user id.

let request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else { // response == 200
    let content = JSON.parse(body);
    let numberTasks = {};
    let x;
    for (x of content) {
      if (x.completed === true) {
        if (x.userId in numberTasks) {
          numberTasks[x.userId] += 1;
        } else {
          numberTasks[x.userId] = 1;
        }
      }
    }
    console.log(numberTasks);
  }
});
