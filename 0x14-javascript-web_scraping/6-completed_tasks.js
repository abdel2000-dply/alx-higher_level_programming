#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const res = {};
  for (const task of data) {
    if (task.completed) {
      res[task.userId] = (res[task.userId] || 0) + 1;
    }
  }
  console.log(res);
});
