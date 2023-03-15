from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    print(request.json)
    a = request.json['a']
    b = request.json['b']
    return {"sum": a + b}
app.run()
@app.route('/sum2', methods=['POST'])
def ohno():
    a = 0
    b = request.json['data']
    for i in range(len(b)):
        a+=b[i]
    c = {'sum':a}
    return c
app.run()
