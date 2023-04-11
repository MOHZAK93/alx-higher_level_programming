#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (num > 0) {
  let i = 0;
  while (i < num) {
    console.log('X'.repeat(num));
    i++;
  }
} else if (!num) {
  console.log('Missing size');
}
