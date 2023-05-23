from flask import Blueprint, render_template, request, flash, redirect, url_for,  abort
from flask_login import login_required, current_user
from . import db
from models import Aula
import random,string
aulas = Blueprint('aulas',__name__)


@aulas.route('/nova_aula')
@login_required
def nova_aula():
    return render_template("aula.html")

@aulas.route('/nova_aula',methods = ['POST'])
@login_required
def nova_aula_post():
    nome_disciplina = request.form.get('name')
    cod_disciplina = request.form.get('codigo')
    turma = request.form.get('turma')
    data_aula = request.form.get('data_aula')
    cod_auth = (''.join(random.choices(string.ascii_letters,k=5)))

    aula = Aula(nome_disciplina = nome_disciplina,
                cod_disciplina = cod_disciplina,
                turma = turma,
                data_aula = data_aula,
                professor = current_user.matricula,
                cod_auth = cod_auth,
                alunos_presentes = [],
                status = 'OPEN')
    db.session.add(aula)
    db.session.commit()
    return redirect(url_for('aulas.codigo_aula',codigo = aula.cod_auth))

@aulas.route('/presenca')
def presenca():
    return render_template('presenca.html')

@aulas.route('/codigo_aula/<codigo>',methods = ['POST','GET'])
@login_required
def codigo_aula(codigo):
    if request.method == 'POST':
        aula = Aula.query.filter_by(cod_auth = codigo).first()
        aula.status = 'CLOSED'
        db.session.commit()
        return "<p> Chamada fechada<p>"
    else:
        return render_template('codigo_aula.html',codigo = codigo)

@aulas.route('/presenca',methods = ['POST'])
def presenca_post():
    cod_aula = request.form.get('cod_aula')
    matricula_aluno = request.form.get('matricula')
    nome_aluno = request.form.get('nome')
    aula = Aula.query.filter_by(cod_auth=cod_aula).first()
    if not aula:
        flash("Aula não cadastrada no sistema",'error')
        return redirect(url_for('aulas.presenca'))
    if aula.status == 'CLOSED':
        flash("Chamada já encerrada",'error')
        return redirect(url_for('aulas.presenca'))
    print(aula.alunos_presentes)
    aula.alunos_presentes.append([nome_aluno, matricula_aluno])
    db.session.commit()
    flash('Presença registrada com sucesso!','info')
    return render_template('presenca.html',nome = nome_aluno, matricula = matricula_aluno, data = aula.data_aula,
                           turma = aula.turma, disc = aula.nome_disciplina)

@aulas.route('/turmas')
@login_required
def turmas():
    matricula_prof = current_user.matricula
    turmas = Aula.query.filter_by(professor = matricula_prof).all()
    turmas_json =[]
    for i in turmas:
        turmas_json.append(i.to_dict())

    return render_template('turmas.html',turmas = turmas_json)

@aulas.route('/aula/<id>')
@login_required
def show_aula(id):
    aula = Aula.query.filter_by(id = id).first()
    if aula:
        return render_template('show_aula.html', aula = aula.to_dict())
    else:
        abort(404)













