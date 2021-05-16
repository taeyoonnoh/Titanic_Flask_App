from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
# from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://bf8c8707d1574c:ab408a57@us-cdbr-east-03.cleardb.com/heroku_aa8bfca22b8aff8"

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app,db)

    from titanic_app.routes import (main_route,edit_route,visualization_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(edit_route.bp, url_prefix='/edit')
    app.register_blueprint(visualization_route.bp, url_prefix='/visualization')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


