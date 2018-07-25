var Components = {
  init: function() {
    (function($) {
      $(document).on("formset:added", function(event, $row, formsetName) {
        if (formsetName.toLowerCase().indexOf("editorial") !== -1) {
          // editorial blocks added by the component admin need to be manually
          // initialised.
          //
          // taken from:
          // https://github.com/django-ckeditor/django-ckeditor/blob/master/ckeditor/static/ckeditor/ckeditor-init.js
          var textareas = Array.prototype.slice.call(
            document.querySelectorAll("textarea[data-type=ckeditortype]")
          );
          for (var i = 0; i < textareas.length; ++i) {
            var t = textareas[i];
            if (
              t.getAttribute("data-processed") == "0" &&
              t.id.indexOf("__prefix__") == -1
            ) {
              t.setAttribute("data-processed", "1");
              var ext = JSON.parse(
                t.getAttribute("data-external-plugin-resources")
              );
              for (var j = 0; j < ext.length; ++j) {
                window.CKEDITOR.plugins.addExternal(
                  ext[j][0],
                  ext[j][1],
                  ext[j][2]
                );
              }
              window.CKEDITOR.replace(
                t.id,
                JSON.parse(t.getAttribute("data-config"))
              );
            }
          }
        }
      });
    })(window.django.jQuery);
  }
};

module.exports = Components;
