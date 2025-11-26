from flask import Flask, render_template, request
from pydantic import ValidationError
from schemas import DayUpdatePayload, DateModel
from db_connector import db_get_day, db_create_table_if_not_exists, add_test_day_data

db_create_table_if_not_exists()
add_test_day_data()

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong", 200

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_day/<string:date_str>")
def get_day(date_str):
    try:
        validated_date = DateModel(day=date_str)
    except ValidationError as e:
        return "invalid date format", 400
    except Exception as e:
        return "internal server error", 500

    day_data = db_get_day(validated_date.day.isoformat())
    if day_data is None:
        return "day not found", 404
    return day_data, 200

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