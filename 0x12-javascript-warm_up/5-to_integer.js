#!/usr/bin/node

/* prints My number: <first argument converted in integer> if the first argument can be converted to an integer: */

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argv[2]));
}
