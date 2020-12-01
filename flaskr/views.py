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
		'SELECT p.pid, Pname,Age,Gender,DateofAdm'
		' FROM patient p'
		).fetchall()
	return render_template('index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Pname = request.form['Pname']
        Age = request.form['Age']
        Gender = request.form['Gender']
        BedNo=request.form['BedNo']
        diagnosis=request.form['diagnosis']
        docname=request.form['docname']
        surgery=request.form['surgery']


        error = None

        if not Pname:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO patient (Pname,Age,Gender,BedNo,diagnosis,docname,surgery)'
                ' VALUES (?, ?, ?,?,?,?,?)',
                (Pname,Age,Gender,BedNo,diagnosis,docname,surgery)    
            )
            db.commit()
            return redirect(url_for('views.index'))

    return render_template('create.html')

@bp.route('/details/<int:pid>', methods=('GET', 'POST'))        
def details(pid):
	db=get_db()
	posts=db.execute(
    	'SELECT p.pid,BedNo'
    	' FROM patient p'
    	' WHERE p.pid={}'.format(pid)
    	).fetchone()
	Diagnosis=db.execute(
    	'SELECT p.pid,diagnosis'
    	' FROM patient p'
    	' WHERE p.pid={}'.format(pid)
    	).fetchone()
	docname=db.execute(
        'SELECT p.pid,docname'
        ' FROM patient p'
        ' WHERE p.pid={}'.format(pid)
    	).fetchone()
	surgery=db.execute(
    	'SELECT q.pid,surgery'
    	' FROM patient q'
    	' WHERE q.pid={}'.format(pid)
    	).fetchone()
	return render_template('details.html', posts=posts,Diagnosis=Diagnosis,docname=docname,surgery=surgery)
