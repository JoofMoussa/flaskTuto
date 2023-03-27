from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/succes/<nom>')
def succes(nom):
	return 'Bienvenu %s' % nom
@app.route('/login',methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		user=request.form['nom']
		return redirect(url_for('succes',nom=user))
	else:
		user=request.args.get('nom')
		return redirect(url_for('succes',nom=user))

