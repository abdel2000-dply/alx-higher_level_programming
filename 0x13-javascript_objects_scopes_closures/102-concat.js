#!/usr/bin/node

const fs = require('fs');

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destPath = process.argv[4];

const fileA = fs.readFileSync(fileAPath, 'utf-8');
const fileB = fs.readFileSync(fileBPath, 'utf-8');

fs.writeFileSync(destPath, fileA + fileB);
