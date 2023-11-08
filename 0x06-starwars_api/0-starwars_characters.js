#!/usr/bin/node

const id = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterPromises = movie.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
	request(characterUrl, (err, response, body) => {
	  if (err) {
	    reject(err);
	  } else if (response.statusCode === 200) {
	    resolve(JSON.parse(body).name);
	  } else {
	    reject('Error Code: ' + response.statusCode);
	  }
	});
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    console.log('Error Code: ' + response.statusCode);
  }
});
