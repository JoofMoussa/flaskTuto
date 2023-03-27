from flask import Flask
app = Flask(__name__)
@app.route('/mapage/<int:ID>')
def numero(ID):
	return 'Mon numero est le : %d' % ID
@app.route('/bulletin/<float:manote>')
def mesnotes(manote):
	return 'Note de Devoir %f' % manote

