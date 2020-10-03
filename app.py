from flask import *
app = Flask(__name__)





@app.route('/')
def home():
    name = "Tuck }"
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run()