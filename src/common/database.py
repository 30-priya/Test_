import uuid

from sqlalchemy import create_engine, String, Column
from flask_sqlalchemy import SQLAlchemy


def generate_uuid():
    return str(uuid.uuid4())


class Database:
    db= None
    Base_model = None
    @staticmethod
    def initialize(app):
        # Database.db = SQLAlchemy(app, engine_options={'sslmode': 'verify-ca', 'sslrootcert': "src/secrets/server-ca.pem",
        #                                      'sslcert': "src/secrets/client-cert.pem",
        #                                      'sslkey': "src/secrets/client-key.pem"})
        Database.db = SQLAlchemy(app)
        class Base(Database.db.Model):
            __abstract__ = True

            id = Column(String(36), primary_key=True, default=generate_uuid, nullable=False)
            created_at = Column(Database.db.DateTime, default=Database.db.func.now())
            updated_at = Column(Database.db.DateTime, default=Database.db.func.now(), onupdate=Database.db.func.now())
        Database.Base_model = Base
    