from flask import Flask, request
s92={'type':'92', 'price': 50, 'volume': 0, 'money':0, 'tank': 0}
s95={'type':'95', 'price': 50, 'volume': 0, 'money':0, 'tank': 0}
s98={'type':'98', 'price': 50, 'volume': 0, 'money':0, 'tank': 0}
app = Flask(__name__)
@app.route('/refuel/', methods=['POST'])
def refuel():
    if request.json['type'] == 92:
        k=request.json.get['volume']
        if k == None:
            k = request.json['money']
            if s92['tank']>=k/s92['price']:
                s92['money']+=k
                s92['tank']-=k/s92['price']
                s92['volume'] += k / s92['price']
                return {'status': 'ok'}
            else:
                return {'status': 'fail', 'text': 'not enough fuel'}
        elif k!= None and s92['tank']>=k:
            s92['volume'] += k
            s92['money'] = s92['money'] + s92['price'] * k
            s92['tank'] -= k
            return {'status': 'ok'}
        else:
            return {'status': 'fail', 'text': 'not enough fuel'}
    elif request.json['type'] == 95:
        k=request.json.get['volume']
        if k == None:
            k = request.json['money']
            if s95['tank']>=k/s95['price']:
                s95['money']+=k
                s95['tank']-=k/s95['price']
                s95['volume'] += k / s95['price']
                return {'status': 'ok'}
            else:
                return {'status': 'fail', 'text': 'not enough fuel'}
        elif k!= None and s95['tank']>=k:
            s95['volume'] += k
            s95['money'] =s95['money'] + s95['price'] * k
            s95['tank'] -= k
            return {'status': 'ok'}
        else:
            return {'status': 'fail', 'text': 'not enough fuel'}
    elif request.json['type'] == 98:
        k=request.json.get['volume']
        if k == None:
            k = request.json['money']
            if s98['tank']>=k/s98['price']:
                s98['money']+=k
                s98['tank']-=k/s98['price']
                s98['volume'] += k / s98['price']
                return {'status': 'ok'}
            else:
                return {'status': 'fail', 'text': 'not enough fuel'}
        elif k!= None and s98['tank']>=k:
            s98['volume'] += k
            s98['money'] =s98['money'] + s98['price'] * k
            s98['tank'] -= k
            return {'status': 'ok'}
        else:
            return {'status': 'fail', 'text': 'not enough fuel'}
@app.route('/fueltruck/', methods=['POST'])
def fueltruck():
    return {'status': 'ok', 'data': {'92': s92['tank'],'95': s95['tank'], '98': s98['tank']}}
@app.route('/fueltruck/', methods=['POST'])
def fueltruck1():
    if '92' in request.json['data'] and request.json['data']['92']:
        if request.json['data']['92']<=1000:
            s92['tank']+= request.json['data']['92']
        else:
            s92['tank']+= 1000-s92['tank']
    if '95' in request.json['data'] and request.json['data']['95']:
        if request.json['data']['95']<=1000:
            s95['tank']+= request.json['data']['95']
        else:
            s95['tank']+= 1000-s95['tank']
    if '98' in request.json['data'] and request.json['data']['98']:
        if request.json['data']['98']<=1000:
            s98['tank']+= request.json['data']['98']
        else:
            s98['tank']+= 1000-s98['tank']
    return {'status':'ok'}
@app.route('/prices/', methods=['POST'])
def prices():
    if '92' in request.json['data'] and request.json['data']['92']>0:
        s92['price']= request.json['data']['92']
    if '95' in request.json['data'] and request.json['data']['95'] > 0:
        s95['price'] = request.json['data']['95']
    if '98' in request.json['data'] and request.json['data']['98']>0:
        s92['price']= request.json['data']['98']
        

