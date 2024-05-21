#!/usr/bin/node

const request = require("request");
const fs = require("fs");

const url = process.argv[2];
const filepath = process.argv[3];

request.get({ url, encoding: 'utf-8'}, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		fs.writeFile(filepath, body, 'utf-8', err => {
			if (err) {
				console.error(err);
			} else {
				console.log(`Contents of ${url} have been saved to ${filePath}`);
			}
		})
	}
})
