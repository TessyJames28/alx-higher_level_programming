#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((currentElement) => currentElement === searchElement).length;
};
