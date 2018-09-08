// This script fetches and lists all movies title by using the URL
// https://swapi.co/api/films/?format=json

$.get('https://swapi.co/api/films/?format=json', (data) => {
   for (let movies of data.results) {
       $('UL#list_movies').append($('<li></li>').text(movies.title));
   }
});
