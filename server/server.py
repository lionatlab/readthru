from flask import Flask, request
from functions import Read_Part, Send_Bible
app = Flask (__name__)

@app.route('/', methods = ['POST','GET'])
def SendBack():
    month = request.form['month']
    date = request.form['date']
    bible = Read_Part(int(month), int(date))
    send_bible = Send_Bible(bible)
    print(send_bible)
    return send_bible

if __name__ == "__main__":
    app.run()