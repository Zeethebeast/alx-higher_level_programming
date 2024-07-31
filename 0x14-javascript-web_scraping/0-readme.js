#!/usr/bin/node
const fs = require('fs').promises;

async function readFileContent(filepath) {
    try {
        const data = await fs.readFile(filepath, 'utf-8');
        console.log(data);
    } catch (err) {
        console.error(err);
    }
}

const filepath = process.argv[2];

if (!filepath) {
    console.error('Provide a file path as argument');
    process.exit(1);
}

readFileContent(filepath);
