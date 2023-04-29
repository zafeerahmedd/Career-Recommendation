from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:////todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


@app.route("/")
def hello_world():
    return render_template("index.html")
    #return "<h>Hello, World!!</h>"

@app.route("/product")
def products():
    return "This is products page"

if __name__=="__main__":
    app.run(debug=True)