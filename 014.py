type_fuel_dict = {'92': {'volume': 0, 'price': 50}, '95': {'volume': 0, 'price': 50}, '98': {'volume': 0, 'price': 50}}
revenue = 0


@app.route('/refuel/', methods=['POST'])
def refuel():
    print(request.json)
    type_fuel = request.json['type']
    try:
        volume = request.json['volume']
        if type_fuel_dict[type_fuel]['volume'] >= volume:
            type_fuel_dict[type_fuel]['volume'] -= volume
            revenue += volume * type_fuel_dict[type_fuel]['price']
            return {'status': 'ok'}
        else:
            return {'status': 'fail', 'text': 'not enough fuel'}
    except:
        money = request.json['money']
        volume = money // type_fuel_dict[type_fuel]['price']
        if type_fuel_dict[type_fuel]['volume'] >= volume:
            type_fuel_dict[type_fuel]['volume'] -= volume
            revenue += money
            return {'status': 'ok'}
        else:
            return {'status': 'fail', 'text': 'not enough fuel'}


@app.route('/fueltruck/', methods=['POST'])
def fueltruck():
    print(request.json)
    data = request.json['data']
    for key in data:
        type_fuel_dict[key]['volume'] += data[key]
    return {'status': 'ok'}


@app.route('/prices/', methods=['POST'])
def prices():
    print(request.json)
    data = request.json['data']
    for key in data:
        type_fuel_dict[key]['price'] = data[key]
    return {'status': 'ok'}


@app.route('/revenue/', methods=['GET'])
def revenue1():
    return {'revenue': revenue}


app.run(host='0.0.0.0', port=5000)