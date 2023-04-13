#!/usr/bin/node

const Square2 = require('./5-square.js');

class Square extends Square2 {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rect = '';
        for (let j = 0; j < this.height; j++) {
          rect += c;
        }
        console.log(rect);
      }
    }
  }
}

module.exports = Square;
