#!/usr/bin/env node
const request = require('request');

// Base URL of the Star Wars API
const BASE_URL = 'https://swapi-api.alx-tools.com/api/films';

// Get the episode number from the command-line arguments
const episodeNumber = process.argv[2];

if (!episodeNumber) {
  console.error('Usage: ./starwars_movie.js <EPISODE_NUMBER>');
  process.exit(1);
}

// Construct the full URL with the episode number
const url = `${BASE_URL}/${episodeNumber}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    // Parse the JSON response
    try {
      const movieData = JSON.parse(body);
      // Print the movie title
      console.log(movieData.title);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error(`Failed to fetch data: Status Code ${response.statusCode}`);
  }
});
