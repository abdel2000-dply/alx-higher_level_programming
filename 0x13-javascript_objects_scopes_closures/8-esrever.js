#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length; i++) {
    const t = list[list.length - i - 1];
    list[list.length - i - 1] = list[i];
    list[i] = t;
  }
  return list;
};
