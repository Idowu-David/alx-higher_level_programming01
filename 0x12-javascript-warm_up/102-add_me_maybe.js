#!/usr/bin/node

/* This script increments and calls a function */

exports.addMeMaybe = function (x, func) {
  x = x + 1;
  func(x);
};
