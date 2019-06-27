from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user={'username':"Alok Mishra"}
    posts=[
        {"a1":{'username':'kartik'},'body':"I am from Kangra"},
        {'a1':{'username':'Moksh'},'body':"I am from Delhi"}
    ]
    return render_template('index3.html',title='Home',user=user,posts=posts)