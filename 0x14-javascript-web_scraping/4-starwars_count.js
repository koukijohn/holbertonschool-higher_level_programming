#!/usr/bin/node
// This is a script that prints the number of movies where the character
// "Wedge Antilles" is present.

let request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).results;
    let appearances = 0;
    for (let movieTitle of results) {
      for (let characterID of movieTitle.characters) {
        if (characterID.search('/18/') > 0) {
          appearances += 1;
        }
      }
    }
    console.log(appearances);
  }
});
