from flask import Flask, request, session, redirect, url_for, render_template, flash, get_flashed_messages
from functools import wraps 
import sqlite3 


app = Flask(__name__)
app.config.from_object('__config')


def login_required(function):
	@wraps(function)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return function(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap


@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = "Wrong username or password"
			status_code = 401
			return render_template('login.html', error=error), status_code
		else:
			session['logged_in'] = True 
			flash('Welcome! you are logged in')
			return redirect(url_for('tasks'))
	return render_template('login.html', error=error), status_code

@app.route('/logout')
def logout():
	session.pop('logged_in')
	flash("You've been logged out")
	return redirect(url_for('login'))


@app.route('/main')
@login_required 
def tasks():
	return '<h1> This is the tasks placeholder page </h1>'