import sys
from flask import Flask
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
    with open(filename, 'r') as f:
        ethers = f.readlines()
    html = '''
    <h1>RARPD mappings</h1>
    <ul>
    '''
    for line in ethers:
        html = html + '<li>' + line + '</li>'
    html = html + '</ul>'
    return html

@app.route("/tftp")
def tftp():
    return "<h1>TFTP mappings</h1>"

@app.route("/nfs")
def nfs():
    filename = '/etc/exports'
    with open(filename, 'r') as f:
        exports = f.readlines()
    html = '''
    <h1>NFS exports</h1>
    <ul>
    '''
    for line in exports:
        html = html + '<li>' + line + '</li>'
    html = html + '</ul>'
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0')

