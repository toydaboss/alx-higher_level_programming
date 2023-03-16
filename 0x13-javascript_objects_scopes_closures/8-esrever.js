#!/usr/bin/node
exports.esrever = function (list) {
  // Initialize an empty array to store the reversed list
  const reversedList = [];

  // Loop through the original list backwards using a for loop
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the reversed list
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
