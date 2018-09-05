#!/usr/bin/node
// This is a script that will display the status code of a GET request.
let request = require('request');

request(process.argv[2], (error, response) => {
  if (error) {
    console.log('code:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
