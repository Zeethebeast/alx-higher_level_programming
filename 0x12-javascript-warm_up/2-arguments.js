#!/usr/bin/node

const args = process.argv.slice(2);

if (!args[0]) {
	let no = `No argument`;
	console.log(no);
} else if (args[1]) {
	//let one = `Argument found`;
	console.log('Arguments found');
} else {
	//let many = `Arguments found`;
	console.log('Argument found');
};
