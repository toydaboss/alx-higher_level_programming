#!/usr/bin/node
// Initialize a variable to keep track of the number of arguments printed
let numPrinted = 0;

exports.logMe = function (item) {
  // Concatenate the number of arguments printed with the current argument value
  const output = `${numPrinted}: ${item}`;

  // Increment the number of arguments printed
  numPrinted++;

  // Log the output to the console
  console.log(output);
};
