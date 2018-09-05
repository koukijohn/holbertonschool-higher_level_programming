#!/usr/bin/node
// This is a script that prints the title of a Star Wars movie where the
// episode number matches a given integer.
let URL = 'http://swapi.co/api/films/' + process.argv[2];
let request = require('request');

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
