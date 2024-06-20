#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2], 10);

if (!args[2] || isNaN(num) || num <= 0) {
  console.log('Missing size');
}
for (let index = 0; index < num; index++) {
  let row = '';
  for (let j = 0; j < num; j++) {
    row += 'X';
  }
  console.log(row);
}
