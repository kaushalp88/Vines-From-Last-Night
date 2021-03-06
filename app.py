from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import os

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug="true")
