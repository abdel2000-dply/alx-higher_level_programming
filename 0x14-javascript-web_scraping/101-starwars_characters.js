#!/usr/bin/node
const request = require('request');
const util = require('util');
const id = process.argv[2];

const promisifiedRequest = util.promisify(request);
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, async (err, response, body) => {
  if (err) console.log(err);
  const film = JSON.parse(body);

  for (const character of film.characters) {
    try {
      const people = await promisifiedRequest(character, { json: true });
      console.log(people.body.name);
    } catch (err) {
      console.log(err);
    }
  }
});
