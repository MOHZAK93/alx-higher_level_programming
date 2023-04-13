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

  rotate () {
    const k = this.width;
    this.width = this.height;
    this.height = k;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
