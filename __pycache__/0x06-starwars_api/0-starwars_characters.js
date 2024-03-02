#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

function makeRequest (characters, index) {
  if (characters.length === index) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      makeRequest(characters, index + 1);
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    makeRequest(characters, 0);
  }
});
