#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle { // defines a square and inherits from Rectangle
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
