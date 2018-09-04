#!/usr/bin/node
// This module contains a function that returns the reversed version of a list.

exports.esrever = function (list) {
  let x = list.length - 1;
  let reversedList = [];
  while (x >= 0) {
    reversedList.push(list[x]);
    x--;
  }
  return reversedList;
};
