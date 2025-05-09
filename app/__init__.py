import os

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('FLASK_SECRET_KEY'),
        DATABASE=os.path.join(app.instance_path, 'we-move.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"
    
    @app.route("/")
    def index():
        return render_template('index.html')
    
    from app.database import db
    db.init_app(app)

    from app.campaigns import bp
    app.register_blueprint(bp, url_prefix="/campaigns")

    from app.users import bp
    app.register_blueprint(bp, url_prefix="/users")

    from app.donations import bp
    app.register_blueprint(bp, url_prefix="/donations")

    return app