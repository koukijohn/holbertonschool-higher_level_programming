#!/usr/bin/node
// This is a script that writes a string to a file.
let fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
