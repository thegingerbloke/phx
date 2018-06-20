var path = require("path");

module.exports = {
  entry: "./src/js/main.js",
  output: {
    path: path.resolve(__dirname, "build/_assets/js/"),
    filename: "main.js"
  },
  mode: "production"
};
