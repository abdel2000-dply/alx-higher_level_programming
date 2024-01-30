#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) console.log(err);
  const film = JSON.parse(body);
  for (const character of film.characters) {
    request(character, (err, response, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  }
});
