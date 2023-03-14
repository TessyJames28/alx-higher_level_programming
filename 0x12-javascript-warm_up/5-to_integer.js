#!/usr/bin/node
// script that convert string argument to numbers if 1st arg is convertible

const val = process.argv[2];

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(val, 10));
}
