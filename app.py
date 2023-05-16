from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS,cross_origin
from src.common.database import Database
db = SQLAlchemy()
load_dotenv('.env')
def create_app():
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}'
    app.secret_key = 'd378c67c9c532726b96802eed6ced21389ab414b4eb69c9b'
    Database.initialize(app)
    Migrate(app,Database.db)
    def register_models(app):
        with app.app_context():
            Database.db.create_all()
    def register_extensions(app):
        Database.db
    register_extensions(app)
    register_models(app)
    return app
app = create_app()


from src.controllers.add_items import create_item_blueprint
app.register_blueprint(create_item_blueprint)
from src.controllers.create_user import user_blueprint
app.register_blueprint(user_blueprint)
from src.controllers.items_list import list_items_blueprint
app.register_blueprint(list_items_blueprint)



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)