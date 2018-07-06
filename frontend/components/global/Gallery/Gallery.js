var Gallery = {
  els: {
    gallery: ".js-Gallery",
    galleryItems: ".js-Gallery-item"
  },

  init: function() {
    this.current = 0;

    this.gallery = document.querySelector(this.els.gallery);
    if (!this.gallery) return false;

    this.galleryItems = this.gallery.querySelectorAll(this.els.galleryItems);

    if (this.galleryItems.length < 2) {
      return false;
    }

    setTimeout(this.transition.bind(this), 3000);
  },

  transition: function() {
    for (var i = 0; i < this.galleryItems.length; i++) {
      this.galleryItems[i].style.opacity = 0;
    }
    this.current =
      this.current != this.galleryItems.length - 1 ? this.current + 1 : 0;
    this.galleryItems[this.current].style.opacity = 1;

    setTimeout(this.transition.bind(this), 3000);
  }
};

module.exports = Gallery;
