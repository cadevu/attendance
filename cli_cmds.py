from flask.cli import AppGroup
from app import db
from app.models import Aula, Professor
from .seed import profs, aulas
seed_cli = AppGroup('seed')
@seed_cli.command('profs')
def seed_profs():
    for prof in profs:
        db.session.add(Professor(**prof))
    db.session.commit()
@seed_cli.command('aulas')
def seed_aulas():
    for aula in aulas:
        db.session.add(Aula(**aula))
    db.session.commit()
