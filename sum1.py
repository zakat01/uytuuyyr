from flask import Flask, request
app = Flask(__name__)
@app.route('/sum/', methods=['POST'])
def hello_world():
    print(request.json)
    a = request.json['a']
    b = request.json['b']
    return {"sum": a + b }
app.run(host='0.0.0.0', port=5000)
