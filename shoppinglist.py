from flask import Flask, request
app = Flask(__name__)
shop_dict = {}
@app.route('/shoppinglist/new/', methods=['POST'])
def shoppinglist():
    num = request.json["new_list"]
    if num in shop_dict:
        return {"status": "fail"}
    shop_dict[f"{num}"] = {}
    print(shop_dict)
    return {"status": "ok"}
@app.route('/shoppinglist/add/', methods=['POST'])
def shoppinglist2():
    data = request.json["data"]
    num = request.json["list"]
    for i in data:
        shop_dict[f"{num}"][i] = data[i] + 1
    return "nnn6"
@app.route('/shoppinglist/getlist/', methods=['POST'])
def shoppinglist3():
    num = request.json["list"]
    print(shop_dict[f"{num}"])
    return shop_dict[f"{num}"]
app.run(host='0.0.0.0', port=5004)