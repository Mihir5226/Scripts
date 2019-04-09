var tinycolor = require('tinycolor2');

var color = tinycolor("red");
color.getFormat();
color = tinycolor({r:255,g:255,b:255});
color.getFormat();

console.log(`This is cool: ${color}`);