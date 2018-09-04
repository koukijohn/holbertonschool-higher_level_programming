#!/usr/bin/node
// This module contains a class Square that defines a square and inherits from
// Square of module 5-square.js

const SquareC = require('./5-square');

class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let x = 0;
    let y = 0;
    let square = '';
    for (; y < this.height; y++) {
      for (; x < this.width; x++) {
        square += c;
      }
      console.log(square);
    }
  }
}

module.exports = Square;
