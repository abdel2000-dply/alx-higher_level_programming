#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) console.error(err);
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) console.error(err);
  });
});
