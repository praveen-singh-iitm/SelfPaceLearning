from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/register")
def home():
    return render_template("register.html")

@app.route("/confirmation", methods=["POST","GET"])
def confirmation():
    if request.method=="POST":
        n=request.form.get("name")
        c=request.form.get("city")
        pn=request.form.get("phonenumber")
        return render_template("confirm.html",name=n,city=c,phonenumber=pn)



if __name__=="__main__":
    app.run(debug=True)