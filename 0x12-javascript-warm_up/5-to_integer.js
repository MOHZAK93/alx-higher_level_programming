#!/usr/bin/node
const Arg = parseInt(process.argv[2]);
if (!Arg) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Arg);
}
