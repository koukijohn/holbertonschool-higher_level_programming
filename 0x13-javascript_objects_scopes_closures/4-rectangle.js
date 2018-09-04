#!/usr/bin/node
// This module will print a square.
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let x;
    let y;
    for (y = 0; y < this.height; y++) {
      let square = '';
      for (x = 0; x < this.width; x++) {
        square += 'X';
      }
      console.log(square);
    }
  }
  rotate () {
    let temp;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double () {
    this.width = (this.width) * 2;
    this.height = (this.height) * 2;
  }
}
module.exports = Rectangle;
