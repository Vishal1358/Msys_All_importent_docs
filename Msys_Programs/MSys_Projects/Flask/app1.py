from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def about():
    name = "Tony"
    return render_template("about.html", name=name)

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)
