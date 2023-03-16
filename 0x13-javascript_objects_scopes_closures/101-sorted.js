#!/usr/bin/node
const { dict } = require('./101-data.js');

const newDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (newDict[occurrences] === undefined) {
    newDict[occurrences] = [userId];
  } else {
    newDict[occurrences].push(userId);
  }
}

console.log(newDict);
