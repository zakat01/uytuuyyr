from flask import Flask, request

app = Flask(__name__)

dish = {'Маленькая': [], 'Средняя': []}

@app.route('/clearall/', methods=['POST'])
def uwu1():
    dish = {'Маленькая': [], 'Средняя': []}
    return {'status': 'ok'}

@app.route('/wash/', methods=['POST'])
def uwu2():
    print(request.json)
    type = request.json['type']
    color = request.json['color']
    dish[type].append(color)
    print(dish)
    return {'status': 'ok'}



@app.route('/take/', methods=['POST'])
def uwu3():
    print(request.json)
    type = request.json['type']
    if dish[type] == []:
        return {'status': 'fail'}
    else:
        dishka = dish[type].pop()
        res = {'status': 'ok', 'color': dishka}
        print(res)
        return res

app.run(host='0.0.0.0', port=5000)