from flask import Flask
import os

application = Flask(__name__)   # IMPORTANT: name must be 'application'

@application.route('/')
def home():
    return "Hello from Beanstalk 🚀"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)