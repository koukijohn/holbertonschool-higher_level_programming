#!/usr/bin/node
// This script will get the contents of a webpage and store it in a file.

let request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else { // response == 200
    let content = body;
    let fs = require('fs');
    fs.writeFile(process.argv[3], content, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
