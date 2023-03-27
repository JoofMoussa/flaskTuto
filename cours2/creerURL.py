from flask import Flask, redirect, url_for
app = Flask(__name__)
app.config['DEBUG']=True
@app.route('/admin')
def admin():
	return 'Bonjour Admin'
@app.route('/invite/<invite>')
def hote(invite):
	return 'Bonjour %s! Connecte comme  invite' %  invite
@app.route('/user/<nom>')
def utilisateur(nom):
	if nom=='admin':
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('hote',invite=moussa))

