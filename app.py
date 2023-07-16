from flask import Flask, render_template , request,flash
from flask_sqlalchemy import SQLAlchemy
import time
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///data.db'      
db=SQLAlchemy(app)
class data(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False )
    email = db.Column(db.String(80),nullable=False )
    msg = db.Column(db.String(120), nullable=False )
    
    def __repr__(self) -> str:
        return f"{self.sno}-{self.email}-{self.msg}"

app.secret_key = '159'

    


app.config['SQLALCHEMY_BINDS'] = {
    'ad': 'sqlite:///admin.db'
}
ad = db

class admin(ad.Model):
    id=ad.Column(ad.String(20),primary_key=True)
    pss=ad.Column(ad.Integer)

with app.app_context():
    db.create_all()
    ad.create_all()

@app.route("/", methods = ['GET', 'POST'])
def contact():
    
    if(request.method=='POST'):
        

        name = request.form['name']
        email = request.form['email']
        msg = request.form['msg']
        temp=data(name=name,email=email,msg=msg)
        db.session.add(temp)
        db.session.commit()
        loggedin=True
        flash('Your Message was Delivered Successfully', 'success')
        

    alldata=data.query.all()
    return render_template('index.html')    
 

@app.route("/login" ,methods = ['GET', 'POST'])
def show():
    # new_user = admin(id='abdul', pss=156)
    # ad.session.add(new_user)
    # ad.session.commit()
    # print("successfully added")
    if(request.method=='POST'):
        
        email = request.form.get('email')
        password = int(request.form.get('pass'))
        
        acc=admin.query.all()
        
        
        for u in acc:
            row=u.id
            row2=u.pss
            
        if email == row and password == row2:
            print("login success")
            alldata = data.query.all()
            
            return render_template('alldata.html',alldata=alldata) 
            
        else:
            print("access denied")

        


    return render_template('alldata.html')


if __name__=="__main__":
    app.run(debug=True)

