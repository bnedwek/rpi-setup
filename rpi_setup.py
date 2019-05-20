import sys
import jinja2
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    html = '''
    <h1>Raspberry Pi setup</h1>
    <ul>
        <p><a href='./rarp'>RARP mapping</a></p>
        <p><a href='./tftp'>TFTP mapping</a></p>
        <p><a href='./nfs'>NFS shares</a></p>
    </ul>
    '''
    return html

@app.route("/rarp")
def rarp():
    filename = '/etc/ethers'
    pairs = []
    with open(filename, 'r') as f:
        for line in f: 
            pair = line.split()
            pairs.append(pair)
    html = render_template('list_pairs.html', title='RARP mappings', pairs=pairs)
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
    html = render_template('list_pairs.html', title='NFS shares', pairs=pairs)
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0')

