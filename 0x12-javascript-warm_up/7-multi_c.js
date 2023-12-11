#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isnan(x) || x < 0) {
  console.log('missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('c is fun');
  }
}
