#!/usr/bin/node
const request = require('request');
const id = 18;
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.log(err);

  const data = JSON.parse(body);
  const films = data.results.reduce((count, film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)) {
      return count + 1;
    }
    return count;
  }, 0);
  console.log(films);
});
