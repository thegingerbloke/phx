var path = require("path");

module.exports = {
  entry: {
    site: "./frontend/js/site.js",
    admin: "./frontend/js/admin.js",
    serviceWorker: "./frontend/js/service-worker.js"
  },
  output: {
    path: path.resolve(__dirname, "frontend/static/js/"),
    filename: "[name].js"
  },
  mode: "production"
};
