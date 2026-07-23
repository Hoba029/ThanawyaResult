from flask import Flask, render_template, request
from grades import generate_result

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    name = request.form["name"].strip()
    seat = request.form["seat"].strip()
    section = request.form["section"]

    grades, total, full, percent, status = generate_result(seat, section)

    return render_template(
        "result.html",
        name=name,
        seat=seat,
        section=section,
        grades=grades,
        total=total,
        full=full,
        percent=percent,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)