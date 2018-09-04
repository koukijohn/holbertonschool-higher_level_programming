#!/usr/bin/node
// This module will print a square.
class Rectangle {
  constructor(w, h, print) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      }
    this.print = function() {
      let x;
      let y;
      for (y = 0; y < h; y++) {
	let square = '';
	for (x = 0; x < w; x++) {
	  square += 'X';
	  }
	console.log(square);
	}
    }
    }
}
module.exports = Rectangle;
