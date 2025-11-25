from os import getenv
from flask import Flask, render_template, request
from pydantic import ValidationError
from schemas import DayUpdatePayload
from datetime import datetime

MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_DB = getenv("MYSQL_DB")

print(datetime.now().isoformat())

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong", 200

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update_day", methods=["POST"])
def update_day():
    try:
        payload = DayUpdatePayload(**request.json)
    except ValidationError as e:
        return "invalid payload", 400
    except Exception as e:
        return "internal server error", 500

    # placeholder 
    return "day updated", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=23186)