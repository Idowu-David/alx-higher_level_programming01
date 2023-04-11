#!/usr/bin/node

/* This script prints the addition of 2 integers */

const argv = process.argv;
function add (a, b) {
  return a + b;
}

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
console.log(add(a, b));
