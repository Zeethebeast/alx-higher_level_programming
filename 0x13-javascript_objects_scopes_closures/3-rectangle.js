#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      //return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let index = 0; index <= this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
