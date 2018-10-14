from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import db, create_app
from info.models import *

app = create_app('developement')
manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manage.run()
