var path = require("path");

module.exports = {
  entry: "./frontend/js/main.js",
  output: {
    path: path.resolve(__dirname, "frontend/static/js/"),
    filename: "main.js"
  },
  mode: "production"
};
