var Offline = require("../components/global/Offline/Offline");
var newWindowLinks = require("./site/new-window-links");
var nav = require("../components/global/Nav/Nav");
var hero = require("../components/global/Hero/Hero");
var gallery = require("../components/global/Gallery/Gallery");
var FixturesList = require("../components/global/FixturesList/FixturesList");
var embed = require("../components/content/Embed/Embed");

Offline.init();
newWindowLinks.init();
nav.init();
hero.init();
gallery.init();
FixturesList.init();
embed.init();
