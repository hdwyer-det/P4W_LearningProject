# Import dependencies
from flask import Flask
from flask import render_template
from flask import request

# Global variables
is_logged_in = False

# Create an instance of the Flask class in the app variable
app = Flask(__name__)


# Define the route for the index page at domain root
@app.route("/", methods=["POST", "GET"])
@app.route("/index.html", methods=["GET", "POST"])
def index_page():
    global is_logged_in
    return render_template("index.html", logged_in=is_logged_in), 200


# Initialise the Flask application
if __name__ == "__main__":
    app.run(debug=True)
