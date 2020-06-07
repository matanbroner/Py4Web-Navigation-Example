(function () {
  var main_app = {
    props: ["get_posts_url", "create_post_url", "get_about_url", "delete_all"],
    // Notice how we never actually use the get_about_url here!
    // That's because we pass it down to the child AboutPage component.
    data: {},
    methods: {},
  };

  main_app.data = function () {
    var data = {
      page: 1, // There are currently 2 pages, 1 = home and 2 = about
      posts: [],
      new_post: "",
      get_url: this.get_posts_url,
      create_url: this.create_post_url,
      about_url: this.get_about_url,
      delete_url: this.delete_all,
    };
    main_app.methods.load.call(data);
    return data;
  };

  main_app.methods.load = function () {
    let self = this;
    axios.get(self.get_url).then((res) => {
      self.posts = res.data.posts;
    });
  };

  main_app.methods.create_new_post = function () {
    if (this.new_post.length == 0) {
      return;
    }
    let self = this;
    axios
      .post(self.create_url, {
        content: self.new_post,
      })
      .then((res) => {
        self.posts.push({
          id: res.data.id,
          content: self.new_post,
        });
        self.new_post = "";
      });
  };

  main_app.methods.delete_all_posts = function () {
    let self = this;
    axios.get(self.delete_url).then(() => {
      self.posts = [];
    });
  };

  // This route changes pages, super simple
  main_app.methods.route = function (page_num) {
    this.page = page_num;
  };

  utils.register_vue_component(
    "mainapp",
    "components/main_app/main_app.html",
    function (template) {
      main_app.template = template.data;
      return main_app;
    }
  );
})();
