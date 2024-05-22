#!/usr/bin/node

const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf8', (error, content) => {
  if (error) {
    console.error('Error reading the file:', error);
  } else {
    console.log(content);
  }
});