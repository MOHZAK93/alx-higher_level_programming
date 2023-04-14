#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let len = list.length;
  let i = 0;
  while (len--) {
    newList[i] = list[len];
    i++;
  }
  return (newList);
};
