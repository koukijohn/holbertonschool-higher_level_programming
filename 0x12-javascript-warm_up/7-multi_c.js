#!/usr/bin/node
const output = 'C is fun';
let x = 0;
if (process.argv[2] > 0) {
  while (x !== parseInt(process.argv[2])) {
    console.log(output);
    x++;
  }
} else if (process.argv[2] < 0) {
} else {
  console.log('Missing number of occurrences');
}
