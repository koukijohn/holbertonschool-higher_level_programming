#!/usr/bin/node
// This module contains a function that returns the number of occurrences in a
// list.

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  let x = 0;
  while (x < list.length) {
    if (list[x] === searchElement) {
      occurences += 1;
    }
    x++;
  }
  return occurences;
};
