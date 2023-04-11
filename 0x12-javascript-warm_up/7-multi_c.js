#!/usr/bin/node
let num = parseInt(process.argv[2]);

if (num) {
  while (num) {
    console.log('C is fun');
    num--;
  }
} else {
  console.log('Missing number of occurrences');
}
