
from flask import Flask, render_template,request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/profile')
def profile():
    return render_template('/profile.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
       uname =  request.form['username']
       pword =  request.form['password']
       print(uname,pword)
       ='select * from ibm_db2
    return render_template('/login.html')
htmt,
if __name__ == '__main__':
    app.run(debug=True)
