from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Version 2 - Blue Environment"

if __name__ == "__main__":
    app.run()