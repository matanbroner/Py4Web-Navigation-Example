// This is a sample page, basically an empty component

(function () {
  var sample_page = {
    props: [],
    methods: {},
  };

  sample_page.data = function () {
    return {};
  };

  utils.register_vue_component(
    "samplepage",
    "components/sample_page/sample_page.html",
    function (template) {
      sample_page.template = template.data;
      return sample_page;
    }
  );
})();
