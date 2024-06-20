#!/usr/bin/node
const args = process.argv;

if (args.length < 3) {
  console.log('Not a number');
} else {
  const num = parseInt(args[2], 10);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + num);
  }
}
