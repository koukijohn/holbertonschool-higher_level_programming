#!/usr/bin/node
// This is a script that reads and prints the content of a file.
let fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
