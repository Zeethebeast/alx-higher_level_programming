#!/usr/bin/node

args = process.argv.slice(2);

if (args[0] === undefined) {
	console.log('No argument');
} else {
	args.forEach((arg, index) => {console.log(`${arg}`);
	});
}
