#!/usr/bin/env python
# encoding: utf-8

import os
from app import create_app
from app import db
from app.models import Person
from flask.ext.script  import Manager
from flask.ext.script  import Shell
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Person=Person)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
