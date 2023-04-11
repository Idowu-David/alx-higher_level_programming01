#!/usr/bin/node

/* This script prints a square */

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  const argN = parseInt(argv[2]);
  for (let i = 0; i < argN; i++) {
    const arr = [];
    for (let j = 0; j < argN; j++) {
      arr.push('X');
    }
    console.log(arr.join(''));
  }
}
