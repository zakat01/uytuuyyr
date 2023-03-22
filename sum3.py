from flask import Flask, request
app = Flask(__name__)
@app.route('/sum3/', methods=['POST'])
def hello_world():
    b = request.json.values()
    d = sum(b)
    return {"sum": d }
app.run(host='0.0.0.0', port=5000)
