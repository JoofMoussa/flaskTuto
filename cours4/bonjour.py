from flask import Flask, render_template
app = Flask(__name__)
@app.route('/Bonjour/<user>')
def direBonjour(user):
	return render_template('index.html', nom=user)
