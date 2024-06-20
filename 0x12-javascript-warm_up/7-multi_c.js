#!/usr/bin/node
const args = process.argv;
const str = 'C is fun';
const num = parseInt(args[2], 10);

if (!args[2] || isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < num; index++) {
    console.log(str);
  }
}
