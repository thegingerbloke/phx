module.exports = function() {
  var current = 0;
  var gallery = document.querySelector(".js-Gallery");
  var galleryItems = gallery.querySelectorAll(".js-Gallery-item");

  setTimeout(transition, 3000);

  function transition() {
    for (var i = 0; i < galleryItems.length; i++) {
      galleryItems[i].style.opacity = 0;
    }
    current = current != galleryItems.length - 1 ? current + 1 : 0;
    galleryItems[current].style.opacity = 1;

    setTimeout(transition, 3000);
  }
};
