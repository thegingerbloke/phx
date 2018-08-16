var Hero = {
  els: {
    hero: ".js-Hero",
    heroItems: ".js-Hero-item"
  },
  transitionTime: 4000,

  init: function() {
    this.current = 0;

    this.hero = document.querySelector(this.els.hero);
    if (!this.hero) return false;

    this.heroItems = this.hero.querySelectorAll(this.els.heroItems);

    if (this.heroItems.length < 2) {
      return false;
    }

    // lazyload subsequent images
    for (var i = 1; i < this.heroItems.length; i++) {
      var hero = this.heroItems[i];
      hero.style.backgroundImage = "url(" + hero.dataset.img + ")";
    }

    // start transition once first new bg image has loaded
    var img = new Image();
    img.addEventListener("load", this.queueTransition.bind(this));
    img.src = hero.dataset.img;
  },
  queueTransition: function() {
    setTimeout(this.transition.bind(this), this.transitionTime);
  },
  transition: function() {
    for (var i = 0; i < this.heroItems.length; i++) {
      this.heroItems[i].style.opacity = 0;
    }
    this.current =
      this.current != this.heroItems.length - 1 ? this.current + 1 : 0;
    this.heroItems[this.current].style.opacity = 1;

    this.queueTransition();
  }
};

module.exports = Hero;
