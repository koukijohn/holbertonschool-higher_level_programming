#!/usr/bin/node
// This is a script that prints the number of movies where the character
// "Wedge Antilles" is present.

let URL = 'https://swapi.co/api/people/18/';
let request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).results;
    let movies = 0;
    for (let x = 0; x < results.length; x++) {
      let characters = results[x].characters;
      for (let y = 0; y < characters.length; y++) {
        if (characters[y] === URL) {
          movies += 1;
        }
      }
    }
    console.log(movies);
  }
});
