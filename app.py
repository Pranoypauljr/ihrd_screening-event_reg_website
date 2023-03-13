from flask import Flask,render_template,request,redirect
import time
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
import time
# from timer import countdown,secs
# import threading
# t1 = threading.Thread(target=countdown)
# t1.start()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)
class usr(db.Model):
    user_id=db.Column(db.Integer,primary_key=True)
    user_fname=db.Column(db.String(500),nullable=False)
    user_lname=db.Column(db.String(500),nullable=False)
    user_email=db.Column(db.String(500),nullable=False)
    user_phno=db.Column(db.Integer,nullable=False,unique=True)
    
    def __repr__(self):
        return '<user_data %r>' % self.user_id
count=1
@app.route('/',methods=['POST','GET'])
def index():
    global count
    if(request.method=='POST'):
        ##below code is to cache the primary key value to ensure unique values are assiged to new registrations each time.
        for i in usr.query.all():
            if count==i.user_id:
                count=len(usr.query.all())+1
                break
        ##unique code till here. 
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phno=request.form['phno']
        new_usr=usr(user_id=count,user_fname=fname,user_lname=lname,user_email=email,user_phno=phno)
        db.session.add(new_usr)
        db.session.commit()
        count+=1
        return redirect('/')
    else:
        return render_template('index.html')
@app.route('/admin')
def new():
    user_data=usr.query.all()
    return render_template('admin.html',user_data=user_data)
if __name__== "__main__":
    app.run(debug=True)
