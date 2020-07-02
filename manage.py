from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
engine = SQLAlchemy.create_engine("postgres://kaustubh:12345@localhost:3308/demo_db", echo=True)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://kaustubh:12345@localhost:3308/demo_db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()
