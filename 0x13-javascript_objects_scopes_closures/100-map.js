#!/usr/bin/node

const list = require('./100-data').list;
const newArray = list.map((a, idx) => {
  return a * idx;
});
console.log(list);
console.log(newArray);
