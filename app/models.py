from . import db
from flask_login import UserMixin
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.mutable import MutableList

class Professor(UserMixin,db.Model):
    __tablename__='professores'
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(500), nullable = False)
    email = db.Column(db.String(200), unique = True, nullable = False)
    matricula = db.Column(db.String(9),unique = True, nullable = False)
    password = db.Column(db.String(200))

class Aula(db.Model):
    __tablename__ = 'aulas'
    id = db.Column(db.Integer, primary_key = True)
    nome_disciplina = db.Column(db.String(500), nullable = False)
    cod_disciplina = db.Column(db.String(6), nullable = False)
    turma = db.Column(db.String(2),nullable = False)
    data_aula = db.Column(db.Date,nullable = False)
    professor = db.Column(db.String(9),db.ForeignKey('professores.matricula'))
    alunos_presentes = db.Column(MutableList.as_mutable(db.ARRAY(db.String)))
    cod_auth = db.Column(db.String(5),nullable = False)
    status = db.Column(db.String)

    def to_dict(self):
        return {"nome":self.nome_disciplina,
                'codigo':self.cod_disciplina,
                'turma':self.turma,
                'data_aula':self.data_aula,
                'matricula_prof':self.professor,
                'alunos_presentes':self.alunos_presentes,
                'cod_auth':self.cod_auth}


