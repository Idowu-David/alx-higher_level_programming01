#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
