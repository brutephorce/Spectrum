from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
with open('config.json', 'r') as c:
    params = json.load(c)["params"]
#import pymysql


app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/brutephorce"
db = SQLAlchemy(app)

class Contacts(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80), nullable=False)
    content= db.Column(db.String(80), nullable=False)
    tagline= db.Column(db.String(12), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    



@app.route('/')
def home():
    #posts=Posts.query.filter_by().all()[0:5]
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        msg=request.form.get('msg')
        phone=request.form.get('phone')
        entry=Contacts(name=name,email=email,phone_num=phone,msg=msg)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

@app.route('/post',methods=['GET'])
def post():
    posts=Posts.query.filter_by().all()
    return render_template('post.html',posts=posts)



@app.route('/post/<string:slug>',methods=['GET'])
def post_route(slug):
    post=Posts.query.filter_by(slug=slug).first()
    return render_template('view_post.html',post=post)




if __name__=='__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
