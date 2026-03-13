from flask import Flask

# create flask application

app = Flask(__name__)


# home route

@app.route("/")
def home():
    return "Docker is working! Hello from Flask App."


# second route

@app.route("/test")
def test():
    return "This is a test route for Docker container."


# run the application

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

