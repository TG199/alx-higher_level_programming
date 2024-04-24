#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
  process.exit(0);
}
let max1 = parseInt(process.argv[2]);
let max2 = parseInt(process.argv[3]);

if (max1 < max2) {
  const a = max1;
  max1 = max2;
  max2 = a;
}
for (let i = 4; i < process.argv.length; i++) {
  const num = parseInt(process.argv[i]);
  if (!isNaN(num)) {
    if (num > max1) {
      max2 = max1;
      max1 = num;
    } else if (num > max2) {
      max2 = num;
    }
  }
}
console.log(max2);
