#!/usr/bin/node
const { list } = require('./100-data.js');

const newList = list.map((value, index) => {
  return value * index;
});

console.log('Initial list:', list);
console.log('New list:', newList);
