#!/usr/bin/node
// This function prints the number of argument already printed and the new
// argument value.

let x = 0;
exports.logMe = function (item) {
  let output = x + ': ' + item;
  console.log(output);
  x++;
};
