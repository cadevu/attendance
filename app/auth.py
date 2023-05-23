from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from models import Professor
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth',__name__)
@auth.route('/login')
def login():
    return render_template("login.html")
@auth.route('/login', methods = ['POST'])
def login_post():
    matricula = request.form.get('matricula')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    prof = Professor.query.filter_by(matricula = matricula).first()


    if not prof:
        flash("Professor não cadastrado na base de dados")
        return redirect(url_for('auth.login'))
    if not check_password_hash(prof.password, password):
        print('wrong psw')
        flash("Senha incorreta, tente novamente.")

        return redirect(url_for('auth.login'))
    login_user(prof, remember = remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup',methods = ['POST'])
def signup_post():
    email = request.form.get('email')
    matricula = request.form.get('matricula')
    nome = request.form.get('nome')
    password = request.form.get("password")
    # if len(matricula) > 9:
    #     flash("Matricula no formato inválido")
    #     return redirect(url_for('auth.signup'))

    prof = Professor.query.filter_by(matricula = matricula).first()
    if prof:
      flash('matricula já cadastrada.','error')
      return redirect(url_for('auth.login'))
    print(prof)
    new_prof = Professor(email = email,
                        matricula = matricula,
                        nome = nome,
                        password =  generate_password_hash(password,method='sha256'))
    db.session.add(new_prof)
    db.session.commit()

    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
