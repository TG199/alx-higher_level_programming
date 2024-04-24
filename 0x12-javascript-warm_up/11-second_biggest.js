#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
}
let max1 = parseInt(process.argv[2]);
let max2 = parseInt(process.argv[3]);

if (max1 < max2) {
  const a = max1;
  max1 = max2;
  max2 = a;
}
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] > max1) {
    max2 = max1;
    max1 = process.argv[i];
  }
}
console.log(max2);
