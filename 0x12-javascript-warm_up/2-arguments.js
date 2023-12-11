#!/usr/bin/node

const n = process.argv.length;

if (n <= 2) {
  console.log('No argument');
} else if (n >= 3) {
  console.log('Arguments found');
}
