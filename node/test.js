var path = require("path");

var hello = "Hello from Node JS variable!"
console.log(`printing Variable hello: ${hello}`);

console.log("directory name: " +__dirname);
console.log("directory and file name: " + __filename);

console.log("using PATH module:");
console.log(`Hello from file ${path.basename(__filename)}`);

console.log(`process args: ${process.argv}`)