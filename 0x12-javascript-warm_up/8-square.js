#!/usr/bin/node
// script that prints a square

const val = process.argv[2];
if (isNaN(val) || val === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < val; i++) {
    let sqr = '';
    for (let j = 0; j < val; j++) {
      sqr += 'X' + '';
    }
    console.log(sqr);
  }
}
