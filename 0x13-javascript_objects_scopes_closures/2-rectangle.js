#!/usr/bin/node
class Rectangle {
	constructor(h, w) {
		 if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
            return;
		}
		this.height = h;
		this.width = w;
		}
}
module.exports = Rectangle;
