from flask import Flask, request, jsonify
from openpyxl import load_workbook
import function

app = Flask(__name__)


@app.route('/', methods=['POST'])
def api_sendback_reading():
    load_wb = load_workbook("./bible.xlsx", data_only=True)
    reading_list = function.load_schedule(load_wb)
    month = int(request.form['month'])
    day = int(request.form['day'])
    today_schedule = function.today_schedule(reading_list, month, day)
    return today_schedule


if __name__ == "__main__":
    app.run()
