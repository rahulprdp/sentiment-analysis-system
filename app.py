import flask
from ml import *

from flask import Flask, render_template , request,redirect

app = Flask(__name__)

//Hello world
@app.route('/')
def index() :
    return render_template("index.html")

@app.route('/res', methods=["POST"])
def result() :
    ls=[]
    text1 = request.form.get("text1")
    text2 = request.form.get("text2")
    text3 = request.form.get("text3")
    ls=[text1,text2,text3]

    rest = score(ls)
    
    return render_template("index.html",res = rest)
    
