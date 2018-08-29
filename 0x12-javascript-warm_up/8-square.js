#!/usr/bin/node
if (parseInt(process.argv[2]) > 0) {
  for (let x = 0; x < process.argv[2]; x++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else if (process.argv[2] < 0) {
} else {
  console.log('Missing size');
}
