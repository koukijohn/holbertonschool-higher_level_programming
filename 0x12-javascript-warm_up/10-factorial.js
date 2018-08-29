#!/usr/bin/node
function recursiveFactorial (x) {
  if (isNaN(x)) {
    return (1);
  }
  if (x === 0) {
    return (1);
  } else {
    return (x * recursiveFactorial(x - 1));
  }
}

console.log(recursiveFactorial(process.argv[2]));
