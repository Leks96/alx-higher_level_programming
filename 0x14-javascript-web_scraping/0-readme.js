#!/usr/bin/node

const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf8', (err, res) => {
  if (err) {
    console.error('Error reading the file:', err);
  } else {
    console.log(res);
  }
});