#!/usr/bin/node

/* This script prints x times “C is fun */

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
