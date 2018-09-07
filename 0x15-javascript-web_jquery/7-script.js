// This script fetches and replaces the name of the URL
// https://swapi.co/api/people/5/?format=json

$.get('https://swapi.co/api/people/5/?format=json', (data, status) => {
  $('DIV#character').text(data.name)
});
