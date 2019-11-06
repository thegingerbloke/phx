var Offline = {
  init: function() {
    if ("serviceWorker" in navigator) {
      window.addEventListener("load", function() {
        navigator.serviceWorker.register("/static/js/serviceWorker.js");
      });
    }
  }
};

module.exports = Offline;
