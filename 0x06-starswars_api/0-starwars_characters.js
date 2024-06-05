#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const data = JSON.parse(body);
  for (const film of data.characters) {
    await getCharacter(film).then((data) => console.log(data));
  }
});

async function getCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, async function (error, response, body) {
      if (error) {
        console.error('error:', error);
      }
      const data = JSON.parse(body);
      resolve(data.name);
    });
  });
}
