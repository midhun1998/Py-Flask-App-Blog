from flask import Flask,request, render_template
import sys

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')  
    return render_template("index.html", name = name)

