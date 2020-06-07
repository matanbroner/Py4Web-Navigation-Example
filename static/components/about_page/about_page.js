// This is the about page component, we do not generate it with Python!

(function () {
  var about_page = {
    props: ["url"], // this url is passed from the parent (main_app), not Python!
    data: {},
    methods: {},
  };

  about_page.data = function () {
    var data = {
      about_content: "",
      get_url: this.url,
    };
    about_page.methods.load.call(data);
    return data;
  };

  about_page.methods.load = function () {
    let self = this;
    axios.get(self.get_url).then((res) => {
      self.about_content = res.data.about;
    });
  };

  utils.register_vue_component(
    "about",
    "components/about_page/about_page.html",
    function (template) {
      about_page.template = template.data;
      return about_page;
    }
  );
})();
