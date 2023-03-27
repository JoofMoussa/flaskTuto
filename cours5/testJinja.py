from flask import Flask, render_template
app = Flask(__name__)
@app.route('/resultat')
def result():
	dict={'math':20,'fran':18,'pc':17}
	return render_template('resultat.html', result=dict)

