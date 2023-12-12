#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};
for (const id in dict) {
  if (dict[id] in newDict) {
    newDict[dict[id]] = [];
  }
  newDict[dict[id]].push(id);
}

console.log(newDict);
