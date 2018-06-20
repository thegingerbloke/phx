/*
 * Nav
 */

var navEl = document.querySelector(".js-Nav");
var toggleEl = document.querySelector(".js-Nav-toggle");

function init() {
  toggleEl.addEventListener("click", toggleNav);
}

function toggleNav(e) {
  e.preventDefault();
  navEl.classList.toggle("Nav--open");
}

module.exports = init;
