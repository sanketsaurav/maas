from flask import Flask, jsonify, redirect, render_template
from utils import fetch_page, extract_meta, extract_meta_prop

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/meta/', methods=['GET'])
def meta_redirect():
	return redirect('/')

@app.route('/meta/<path:url>', methods=['GET'])
def meta(url=None):
	if not url.startswith('http'):
		url = 'http://' + url
	response, status = extract_meta(fetch_page(url))
	return jsonify({'status' : status, 'data' : response})

@app.route('/meta/<prop>/<path:url>', methods=['GET'])
def meta_prop(prop=None, url=None):
	if not url.startswith('http'):
		url = 'http://' + url
	response, status = extract_meta_prop(fetch_page(url), prop)
	return jsonify({'status' : status, 'data' : response})

if __name__ == '__main__':
	app.run(debug=True)