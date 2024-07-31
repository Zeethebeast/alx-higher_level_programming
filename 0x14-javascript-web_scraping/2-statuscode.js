#!/usr/bin/node
const request = require('request');

// Get the URL from command-line arguments
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./status_code.js <URL>');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Print the status code in the required format
  console.log(`code: ${response.statusCode}`);
});
