from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/valentine.html")
def valentine():
    return render_template("valentine.html")

@app.route("/404.html")
def error_404():
    return render_template("404.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, port=5050)