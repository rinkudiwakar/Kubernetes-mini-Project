from flask import Flask, render_template, request
from datetime import datetime

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    message=""
    if request.method=="POST":
        name=request.form.get("name")
        message= f"Hello {name}, welcome to the Kubernetes test app!"
    return render_template("index.html",message=message,
                           current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)