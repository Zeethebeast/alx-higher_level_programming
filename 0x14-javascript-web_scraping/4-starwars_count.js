#!/usr/bin/node
const request = require('request');

// Get the API URL from command-line arguments
const apiUrl = process.argv[2];

// Character ID for "Wedge Antilles"
const characterId = 15;

if (!apiUrl) {
  console.error('Usage: ./count_movies_with_character.js <API_URL>');
  process.exit(1);
}

// Function to fetch movies and count those with the character
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    try {
      const data = JSON.parse(body);
      request(data.results[0].characters[15], (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            process.exit(1);
        }
        
        const res = JSON.parse(body);
        console.log((res.films).length)
      });

    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error(`Failed to fetch data: Status Code ${response.statusCode}`);
  }
});
