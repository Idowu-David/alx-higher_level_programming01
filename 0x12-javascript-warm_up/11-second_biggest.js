#!/usr/bin/node

/* This script searches the second biggest integer in the list of arguments. */

const argv = process.argv.slice(2);
const parseArg = [];
for (let i = 0; i < argv.length; i++) {
  parseArg.push(parseInt(argv[i]));
}
if (parseArg.length <= 1) {
  console.log(0);
} else {
  parseArg.sort();
  parseArg.reverse();
  console.log(parseArg[1]);
}
