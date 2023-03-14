#!/usr/bin/node
// script that computes and prints a factorial recursively

function factorial (n) {
  if (isNaN(n) || n === undefined) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

const val = parseInt(process.argv[2], 10);
console.log(factorial(val));
