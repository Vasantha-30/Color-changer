from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def color():
    color = "white"   # default color

    if request.method == "POST":
        color = request.form["color"]   # get input from user

    return render_template("index.html", color=color)

app.run(debug=True)