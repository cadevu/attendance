from . import db
from sqlalchemy.ext.mutable import MutableList
class Aula(db.Model):
    __tablename__ = 'aulas'
    id = db.Column(db.Integer, primary_key = True)
    nome_disciplina = db.Column(db.String(500), nullable = False)
    cod_disciplina = db.Column(db.String, nullable = False)
    turma = db.Column(db.String,nullable = False)
    data_aula = db.Column(db.Date,nullable = False)
    professor = db.Column(db.String,db.ForeignKey('professores.matricula'))
    alunos_presentes = db.Column(MutableList.as_mutable(db.ARRAY(db.String)))
    cod_auth = db.Column(db.String(5),nullable = False)
    status = db.Column(db.String)

    def to_dict(self):
        return {"id":self.id,
                "nome":self.nome_disciplina,
                'codigo':self.cod_disciplina,
                'turma':self.turma,
                'data_aula':self.data_aula,
                'matricula_prof':self.professor,
                'alunos_presentes':self.alunos_presentes,
                'cod_auth':self.cod_auth}

