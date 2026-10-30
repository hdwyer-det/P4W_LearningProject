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

    # If we receive a POST request, then set is_logged_in to be true
    # Otherwise set is_logged_in to be false
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        is_logged_in = True
        print(f"user {email} has logged in with password {password}")
    else:
        is_logged_in = False
    return render_template("index.html", logged_in=is_logged_in), 200


# Initialise the Flask application
if __name__ == "__main__":
    app.run(debug=True)
