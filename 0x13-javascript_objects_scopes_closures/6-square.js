#!/usr/bin/node
const SquareR = require('./5-square');

class Square extends SquareR {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += c;
      }
      console.log(rect);
    }
  }
}

module.exports = Square;
