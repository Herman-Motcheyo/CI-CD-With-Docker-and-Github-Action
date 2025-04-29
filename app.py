from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My First CI/CD Project! </h1>
    <p>This application demonstrates a simple deployment using Docker and GitHub Actions.</p>
    <p>Hello, World! </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
