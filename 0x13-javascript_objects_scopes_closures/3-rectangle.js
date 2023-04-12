#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let j = 0;
    while (j < this.height) {
      console.log('X'.repeat(this.width));
      j++;
    }
  }
}
module.exports = Rectangle;
