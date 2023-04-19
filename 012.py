from flask import Flask, request

app = Flask(__name__)

queue = []


@app.route('/queueclear/', methods=['POST'])
def queueclear1():
    queue = []
    return {"status": 'ok'}

@app.route('/queue/', methods=['POST'])
def queue1():
    person = request.json["person_to_add"]
    queue.append(person)
    return {"status": 'ok'}

@app.route('/queue/', methods=['GET'])
def queue2():
    if queue == []:
       return {"status": 'fail'}
    else:
       name = queue.pop(0)
       res = {"status": 'ok'}
       res["person"] = name
       print(res)
       return res

app.run(host='0.0.0.0', port=5000)

