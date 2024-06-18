#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let text = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        text += 'X';
      }
      if (i !== this.height - 1) {
        text += '\n';
      }
    }
    console.log(text);
  }
}
module.exports = Rectangle;
