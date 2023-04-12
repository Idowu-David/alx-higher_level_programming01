#!/usr/bin/node

/* This script executes a function x times */

exports.callMeMoby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
