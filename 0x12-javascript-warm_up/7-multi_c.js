#!/usr/bin/node
// script that prints x times "C is fun"

const val = process.argv[2];
if (isNaN(val) || val === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < val; i++) {
    console.log('C is fun');
  }
}
