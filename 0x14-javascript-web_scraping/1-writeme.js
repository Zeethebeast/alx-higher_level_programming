#!/usr/bin/node
const fs = require('fs').promises;

async function writeFileContent(filepath, content) {
  try {
    // Write the content to the file using fs.promises.writeFile
    await fs.writeFile(filepath, content, 'utf-8');
  } catch (err) {
    console.error('Error writing to file:', err);
  }
}

// Get the file path and content from the command-line arguments
const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || !content) {
  console.error('Provide a file path and content as arguments');
  process.exit(1);
}

writeFileContent(filepath, content);
