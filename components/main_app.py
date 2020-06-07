from py4web import action, URL, request
from yatl.helpers import XML
from py4web.utils.url_signer import URLSigner
from py4web.core import Fixture


class MainAppComponent(Fixture):

    # The main app leaves spots for all of its props to be passed (prop = data being passed down)
    MAINAPP = """<mainapp 
    get_posts_url={get_posts_url}
    create_post_url={create_post_url}
    get_about_url={get_about_url}
    delete_all={delete_all}
    ></thumbrater>"""

    def __init__(self, url, session, signer=None, db=None, auth=None):
        self.base_url = url
        self.db = db
        self.__prerequisites__ = [session]
        self.signer = signer or URLSigner(session)
        self.args = list(
            filter(None, [session, db, auth, self.signer.verify()]))

        self.define_urls()

        self.create_route(self.get_posts_url, self.get_posts, "GET")
        self.create_route(self.get_about_url, self.get_about, "GET")
        self.create_route(self.delete_all_posts_url,
                          self.delete_all_posts, "GET")
        self.create_route(self.create_post_url, self.create_post, "POST")

    def __call__(self, img_id=None):  # turn our class into HTML
        return XML(MainAppComponent.MAINAPP.format(
            get_posts_url=URL(self.get_posts_url, signer=self.signer),
            create_post_url=URL(self.create_post_url, signer=self.signer),
            get_about_url=URL(self.get_about_url, signer=self.signer),
            delete_all=URL(self.delete_all_posts_url, signer=self.signer)
        ))

    def define_urls(self):
        self.get_posts_url = self.base_url + "/get_posts"
        self.create_post_url = self.base_url + "/create_post"
        self.get_about_url = self.base_url + "/about"
        self.delete_all_posts_url = self.base_url + "/clear"

    def create_route(self, url, method, protocol):
        func = action.uses(*self.args)(method)
        action(url, method=[protocol])(func)

    def get_posts(self):
        posts = self.db(self.db.posts).select().as_list()
        return dict(posts=posts)

    def create_post(self):
        content = request.json.get('content')
        id = self.db.posts.insert(content=content)
        return dict(id=id)

    def delete_all_posts(self):
        self.db(self.db.posts).delete()

    def get_about(self):
        about = """We are a great company with a fantastic user base.
        Be sure to check us out on all social media platforms for updates!
        Copyright PostCo. 2020
        """
        return dict(about=about)
