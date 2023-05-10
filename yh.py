return{"status": "ok"}
@app.route('/prices/', methods=["GET"])
def rev():
    return {"status": "ok", "92": s92["money"], "95": s95["money"], "98": s98["money"]}
@app.route("/default", methods=["GET"])
def defauilt():
    s92["price"] = 50
    s92["volume"] = 0
    s92["money"] = 0
    s92["tank"] = 0

    s95["price"] = 50
    s95["volume"] = 0
    s95["money"] = 0
    s95["tank"] = 0

    s98["price"] = 50
    s98["volume"] = 0
    s98["money"] = 0
    s98["tank"] = 0
    return {"status": "ok"}
@app.route("/revenue/", methods=["GET"])
def revenue():
    print(s92[ "money"]+s95[ "money"]+s98[ "money"])
    return {"status": "ok", "revenue": s92[ "money"]+s95[ "money"]+s98[ "money"]}
if __name__ == "__main__":
    app.run(nost="0.0.0.0" , port=5000)