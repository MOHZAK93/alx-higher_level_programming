#!/usr/bin/node
let num = parseInt(process.argv[2]);

if (num > 0) {
  while (num) {
    console.log('C is fun');
    --num;
  }
} else if (!num) {
  console.log('Missing number of occurrences');
}
