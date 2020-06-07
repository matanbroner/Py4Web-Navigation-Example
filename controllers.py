import uuid

from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner

from yatl.helpers import A
from . common import db, session, T, cache, auth, signed_url

# Import main app component
from .components.main_app import MainAppComponent

# Create instance of main app
app = MainAppComponent('app', session, db=db)

url_signer = URLSigner(session)

# The auth.user below forces login.
@action('index')
@action.uses('index.html', url_signer)
def index():
    # notice that we say app=app() and NOT app=app, the parens. are super important!
    # ie. that's how the __call__ method is used
    return dict(app=app())
