#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num_of_occur = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      num_of_occur += 1;
    }
  }
  return num_of_occur;
}
      
