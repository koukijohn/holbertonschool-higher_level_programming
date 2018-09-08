// This script will fetche and print the San Francisco wind speed by using the
// URL: https://query.yahooapis.com/v1/public
// /yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20
// (select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco
// %2C%20CA%22)&format=json
baseurl = 'https://query.yahooapis.com/v1/public';
urlext = '/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json';
url = baseurl + urlext;
$.get(url, (data) => {
  $('DIV#sf_wind_speed').text(data.query.results.channel.wind.speed);
});
