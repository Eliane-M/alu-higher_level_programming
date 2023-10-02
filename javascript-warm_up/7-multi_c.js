#!/usr/bin/node
const x = process.argv[2];

for (let i = 1; i <= x; i++) {
  if (x === undefined) {
    console.log('Missing number of occurrences');
  } else {
    console.log('C is fun');
  }
}
