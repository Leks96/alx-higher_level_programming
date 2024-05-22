#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

const file = process.argv[2];

fs.readFile(file, 'utf8', function (err, res) {
  // Use fs.readFile() to read the contents of a file specified as a command-line argument
  // 'utf8' specifies the encoding of the file being read

  if (err) {
    // If an error occurs during the file read operation, the 'error' parameter will contain an error object.
    console.error('Error reading the file:', err);

  } else {
    // If the file is read successfully, the 'content' parameter will contain the contents of the file as a string.
    console.log(res);
  }
});