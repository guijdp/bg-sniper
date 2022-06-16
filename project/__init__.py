from flask import Flask

######################################
#### Application Factory Function ####
######################################


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    @app.route("/")
    def home():
        return "Welcome Page"

    return app
