#!/usr/bin/node

const request = require("request");

const apiUrl = process.argv[2];
const charId = 18;

request.get(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		const movies = JSON.parse(body).results;
		const moviesWithChar =  movies.filter(movies => 
			movies.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
		);
		console.log(moviesWithChar.length);
	}
});
