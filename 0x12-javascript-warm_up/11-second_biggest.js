#!/usr/bin/node
if (process.argv.length < 4 || process.argv[2] === undefined) {
  console.log('0');
}
if (process.argv.length >= 4) {
  console.log(process.argv.sort()[process.argv.length - 2]);
}
