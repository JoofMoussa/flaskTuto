from flask import Flask
app = Flask(__name__)
app.config['DEBUG']=True
@app.route('/')
def hello():
	return 'Welcome in ODC'
