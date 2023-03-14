#!/usr/bin/node
// update a const object to change the value of a property

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.value = 89;

console.log(myObject);
