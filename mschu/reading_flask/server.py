from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def api_sendback_reading():
    month = request.form['month']
    day = request.form['day']
    return month+day


if __name__ == "__main__":
    app.run()
