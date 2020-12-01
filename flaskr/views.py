from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from .db import get_db

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
	db = get_db()
	posts = db.execute(
		'SELECT p.id, Pname,Age,Gender,DateofAdm'
		' FROM patient p'
		).fetchall()
	return render_template('index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Pname = request.form['Pname']
        Age = request.form['Age']
        Gender = request.form['Gender']
        error = None

        if not Pname:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO patient (Pname,Age,Gender)'
                ' VALUES (?, ?, ?)',
                (Pname,Age,Gender)    
            )
            db.commit()
	
            return redirect(url_for('views.index'))

    return render_template('create.html')    
