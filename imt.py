from flask import Flask, request

app = Flask(__name__)
@app.route('/imt/', methods=['POST'])
def imt():
    if 'height' in request.json and 'weight' in request.json:
        height = request.json['height']
        weight = request.json['weight']
        return {"status": 'ok', 'imt': int(weight/((height/100)**2))}
    if 'height' in request.json and 'imt' in request.json:
        height = request.json['height']
        imt = request.json['imt']
        return {"status": 'ok', 'weight':int(imt*(height/100)**2)}
    if 'imt' in request.json and 'weight' in request.json:
        imt = request.json['imt']
        weight = request.json['weight']
        return {"status": 'ok', 'height': int(((weight/imt)**0.5)*100)}
app.run(host='0.0.0.0', port=5007)