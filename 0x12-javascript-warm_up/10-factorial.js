#!/usr/bin/node

/* This Script computes and prints a factorial */

function fact (a) {
  if (a === 1) {
    return 1;
  }
  return (a * fact(a - 1));
}

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log(1);
} else {
  console.log(fact(parseInt(argv[2])));
}
