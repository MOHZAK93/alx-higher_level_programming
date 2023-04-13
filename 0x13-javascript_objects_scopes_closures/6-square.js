#!/usr/bin/node
const oldSquare = require('./5-square');
class Square extends oldSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let j = 0;
    while (j < this.height) {
      console.log(c.repeat(this.width));
      j++;
    }
  }
}
module.exports = Square;
