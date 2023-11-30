# Import flask 
from flask import Flask

# Start our app
app = Flask (__name__)

# Routes, Function to define what will we do
@app.route("/")
def helloWorld():
    return('Hello, Flask World!')

# Adding another routes
@app.route("/details")
def details():
    return("My details")

# Run the app
if __name__ == "__main__":
    app.run()