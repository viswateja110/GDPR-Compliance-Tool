from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/details")
def details():
    return render_template("details.html")
@app.route("/check",methods=['GET','POST'])
def check():
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        if fname!='' and lname!='':
            return 'dashboard'
        else:
            return 'please fill all the fields'
    else:
        return 'error'
    
if __name__=='__main__':
    app.run(debug=True)