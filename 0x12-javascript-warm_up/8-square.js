#!/usr/bin/node
const iterations = process.argv[2]
if (parseInt(iterations) > 0) {
  for (let x = 0; x < iterations; x++) {
    console.log('X'.repeat(iterations));
  }
} else if (process.argv[2] < 0) {
} else {
  console.log('Missing size');
}
