from flask import Flask, request
app = Flask(__name__)
@app.route('/nextround/', methods=['POST'])
def hello_world():
    b = request.json['data']
    k = request.json['k']
    n = request.json['n']
    a = 0
    for i in range(n):
        c = b[k]
        if b[i] >= c and b[i]>0:
            a += 1
    return{'res': a }
app.run(host='0.0.0.0', port=5000)
