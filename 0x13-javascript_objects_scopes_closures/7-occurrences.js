#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const l of list) {
    if (l === searchElement) {
      count++;
    }
  }

  return count;
};
