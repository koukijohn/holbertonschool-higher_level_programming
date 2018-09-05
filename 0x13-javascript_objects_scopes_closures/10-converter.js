#!/usr/bin/node
// This function will convert a number from base 10 to another base passed
// as argument

exports.converter = function (base) {
  return function (x) {
    return x.toString(base);
  };
};
