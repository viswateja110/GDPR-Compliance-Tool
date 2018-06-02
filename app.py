from flask import Flask,render_template,request
from formmanagement import Details 


app=Flask(__name__)
app.config['SECRET_KEY']='953c02c58733be2c9831a67c86b6e7c0'
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/details")
def details():
    form=Details()
    return render_template("details.html",form=form)

    
   
    
if __name__=='__main__':
    app.run(debug=True)