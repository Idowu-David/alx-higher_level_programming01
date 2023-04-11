#!/usr/bin/node

/* prints My number: <first argument converted in integer> */
/* if the first argument can be converted to an integer: */

const argv = process.argv;

if (argv[2]) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
