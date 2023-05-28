from flask import Blueprint, render_template, request, flash, redirect, url_for,  abort
from flask_login import login_required, current_user
from . import db
from ..models import Aula
import random,string
aulas = Blueprint('aulas',__name__)


@aulas.route('/new',methods = ['POST','GET'])
@login_required
def nova_aula():
    if request.method == 'GET':
        return render_template("aula.html")
    else:
        nome_disciplina = request.form.get('name')
        cod_disciplina = request.form.get('codigo')
        turma = request.form.get('turma')
        data_aula = request.form.get('data_aula')
        cod_auth = (''.join(random.choices(string.ascii_letters,k=5)))
        print("here")
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
        return redirect(url_for('aulas.codigo_aula',code = aula.cod_auth))

@aulas.route('/presenca')
def presenca():
    return render_template('presenca.html')

@aulas.route('/codigo_aula/<code>',methods = ['GET'])
@login_required
def codigo_aula(code):
    return render_template('codigo_aula.html',codigo = code)
    # if request.method == 'POST':
    #     aula = Aula.query.filter_by(cod_auth = code).first()
    #     aula.status = 'CLOSED'
    #     db.session.commit()
    #     return "<p> Chamada fechada<p>"

@aulas.route('/codigo_aula/<code>',methods = ['POST'])
@login_required
def close_attendance(code):
        aula = Aula.query.filter_by(cod_auth = code).first()
        aula.status = 'CLOSED'
        db.session.commit()
        return redirect(url_for('aulas.show_aula',id = aula.id))


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

@aulas.route('/')
@login_required
def turmas():
    matricula_prof = current_user.matricula
    turmas = Aula.query.filter_by(professor = matricula_prof).order_by(Aula.data_aula.desc()).all()
    turmas_json =[]
    for i in turmas:
        turmas_json.append(i.to_dict())

    return render_template('turmas.html',turmas = turmas_json)

@aulas.route('/<id>')
@login_required
def show_aula(id):
    aula = Aula.query.filter_by(id = id).first()
    if aula:
        return render_template('show_aula.html', aula = aula)
    else:
        abort(404)

@aulas.route('/<int:id>/delete',methods = ['POST','DELETE'])
@login_required
def destroy(id):
    aula = db.get_or_404(Aula, id)
    db.session.delete(aula)
    db.session.commit()
    flash(f"Aula de '{aula.nome}', de id: {aula.id} deletada")

@aulas.route('/<id>/<matricula>/<nome>/delete',methods = ['POST','DELETE'])
@login_required
def destroy_student(id,matricula,nome):
    aula = db.get_or_404(Aula, id)
    aluno = [nome,matricula]
    if aluno in aula.alunos_presentes:
        print(aula.alunos_presentes)
        print(aluno[0])
        print(aluno[1])
        aula.alunos_presentes.remove(aluno)
    db.session.commit()
    return redirect(url_for('aulas.show_aula', id = id))

@aulas.route('/<id>/new_student',methods = ['GET','POST'])
@login_required
def add_student(id):
    if request.method == 'GET':
        return render_template('new_student.html', id = id)
    else:
        aula = db.get_or_404(Aula, id)
        nome = request.form.get('nome')
        matricula = request.form.get('matricula')
        aluno = [nome,matricula]
        aula.alunos_presentes.append(aluno)
        db.session.commit()
        return redirect(url_for('aulas.show_aula',id = id))













