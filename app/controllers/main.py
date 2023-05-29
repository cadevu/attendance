from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..webapp import index
@index.route('/')
def index():
    return render_template('index.html')

main = Blueprint('main',__name__)

@main.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@main.route('/profile/')
@login_required
def profile():
    return render_template("profile.html",nome = current_user.nome, matricula = current_user.matricula)
