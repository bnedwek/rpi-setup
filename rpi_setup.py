import sys
import jinja2
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    html = render_template('index.html')
    return html

@app.route("/rarp")
def rarp():
    filename = '/etc/ethers'
    pairs = []
    with open(filename, 'r') as f:
        for line in f: 
            pair = line.split()
            pairs.append(pair)
    html = render_template('list_pairs.html', title='RARP mappings', headers=['MAC', 'IP'], pairs=pairs)
    return html

@app.route("/tftp")
def tftp():
    return "<h1>TFTP mappings</h1>"

@app.route("/nfs")
def nfs():
    filename = '/etc/exports'
    pairs = []
    with open(filename, 'r') as f:
        for line in f:
            pair = line.split()
            pairs.append(pair)
    html = render_template('list_pairs.html', title='NFS shares', headers=['PATH', 'IP'], pairs=pairs)
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0')

