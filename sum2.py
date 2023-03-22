from flask import Flask, request
app = Flask(__name__)
@app.route('/sum2/', methods=['POST'])
def hello_world():
    data = request.json['data']
    summa = 0
    for i in range(len(data)):
        summa += data[i]
    return {"sum": summa}
app.run(host='0.0.0.0', port=5000)

