from pydoc import render_doc
from flask import *
import hate_speech
app = Flask(__name__,template_folder='template')



@app.route("/")
def hello():
    if request.method == 'POST':
        username = request.form['username']
        marks_pred = hate_speech.
    return render_template("index.html")




@app.route("/sub",methods =['POST'])
def submit():
    if request.method == "POST":
        name = request. form['username']
    return render_template("sub.html",n = name)
if __name__ =="__main__":
    app.run(debug=True) 