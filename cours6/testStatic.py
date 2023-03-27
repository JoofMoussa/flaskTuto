import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Cle Secrete'

def get_db_connection():
	conn = sqlite3.connect('basededonnee.db')
	conn.row_factory = sqlite3.Row
	return conn

@app.route('/')
def index():
	conn = get_db_connection()
	Etudiant = conn.execute('SELECT * FROM Etudiant').fetchall()
	conn.close()
	return render_template('index.html', Etudiant=Etudiant)
	
def get_num(num):
	conn = get_db_connection()
	info = conn.execute('SELECT * FROM Etudiant WHERE Numero = ?', (num,)).fetchone()
	conn.close()
	if info is None:
		abort(404)
	return info
	
@app.route('/<int:num>')
def insererDonnee(num):
	info = get_num(num)
	return render_template('post.html', info=info)
	
@app.route('/ajoutInfo', methods=('GET', 'POST'))
def ajout():
	if request.method == 'POST':
		num = request.form['Numero']
		code = request.form['Code']
		nom = request.form['Nom']
		prenom = request.form['Prenom']
		adr = request.form['Adresse']
		if not num:
			flash('Veuillez entrez le Numero!')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO Etudiant (Numero, Code, Prenom, Nom, Adresse) VALUES (?, ?, ?, ?, ?)',
			(num, code, prenom, nom, adr))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))
	return render_template('ajoutInfo.html')
	
	
@app.route('/<int:id>/modifier', methods=('GET', 'POST'))
def modifier(id):
	info = get_num(id)
	if request.method == 'POST':
		num = request.form['Numero']
		code = request.form['Code']
		nom = request.form['Nom']
		prenom = request.form['Prenom']
		adr = request.form['Adresse']
		if not num:
			flash('Veuillez entrez le Numero!')
		else:
			conn = get_db_connection()
			conn.execute('UPDATE Etudiant SET Numero = ?, Nom = ?,  Prenom = ?, Adresse = ?, Code = ? ' ' WHERE Numero= ?',
			(num, code, nom, prenom, adr, id))
			conn.commit()
			conn.close()
			flash('"{}" a ete ajoute avec succes!'.format(info['Numero']))
			return redirect(url_for('index'))
	return render_template('modifierInfo.html', info=info)
	
@app.route('/<int:id>/supprimer', methods=('POST',))
def supprimer(id):
	info = get_num(id)
	conn = get_db_connection()
	conn.execute('DELETE FROM Etudiant WHERE Numero = ?', (id,))
	conn.commit()
	conn.close()
	flash('"{}" a ete supprime!'.format(info['Numero']))
	return redirect(url_for('index'))
	
	
	
	
	
	
	
	
	
	
	
	
