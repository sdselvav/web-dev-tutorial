from flask import Flask, render_template, request
from helpers import find_house, user

app: Flask = Flask(__name__)

users: list[user] = []
user_number: int = 0


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        animal: str = request.form['animal']

        if fname == '' or lname == '':
            return render_template("quiz.html")

        house: str = find_house(animal)
        new_user: user = user(user_number, fname, lname, house)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", house=house)
    return render_template("quiz.html")


if __name__ == '__main__':
    app.run(debug=True)