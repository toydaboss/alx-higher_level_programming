#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destFile = process.argv[4];

const data1 = fs.readFileSync(sourceFile1);
const data2 = fs.readFileSync(sourceFile2);
const concatenatedData = Buffer.concat([data1, data2]);

fs.writeFileSync(destFile, concatenatedData);
console.log(`The contents of ${sourceFile1} and ${sourceFile2} have been concatenated to ${destFile}`);
