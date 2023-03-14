#!/usr/bin/node
// script that prints the addition of two integers

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
add(num1, num2);
