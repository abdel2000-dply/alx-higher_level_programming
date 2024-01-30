#!/usr/bin/node
const request = require('request');
const id = 18;
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const films = data.results.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)
    );
    console.log(films.length);
  }
});
