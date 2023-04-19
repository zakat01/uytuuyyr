from flask import Flask, request
app = Flask(__name__)
dog_years = {1:14, 1.5:20, 2:24, 3:30, 4:36, 5:40, 6:42, 7:49, 8:56, 9:63, 10:65, 11:71, 12:75}
dog_month = {2:14, 6:5, 8:9}
human_years = {14:1, 20:1.5, 24:2, 30:3, 36:4, 40:5, 42:6, 49:7, 56:8, 63:9, 65:10, 71:11, 75:12}
human_month = {14:2, 5:6, 9:8}
@app.route('/lebo1/', methods=['POST'])



def age():
    if request.json['type'] == 'dog' and request.json['units'] == 'years':
        h = dog_years[request.json['n']]
        print({ 'n': h, 'units': 'years','type': 'human'})
        return { 'n': h, 'units': 'years','type': 'human'}

    elif request.json['type'] == 'human' and request.json['units'] == 'years' and request.json['n'] >= 14:
        d = human_years[request.json['n']]
        print({ 'n': d, 'units': 'years','type': 'dog'})
        return { 'n': d, 'units': 'years','type': 'dog'}

    elif request.json['type'] == 'dog' and request.json['units'] == 'month' and request.json['n'] > 2:
        h = dog_month[request.json['n']]
        print({ 'n': h, 'units': 'years','type': 'human'})
        return { 'n': h, 'units': 'years','type': 'human'}
    elif request.json['type'] == 'dog' and request.json['units'] == 'month' and request.json['n'] == 2:
        h = dog_month[request.json['n']]
        print({'n': h, 'units': 'month', 'type': 'human'})
        return {'n': h, 'units': 'month', 'type': 'human'}
    elif request.json['type'] == 'human' and request.json['units'] == 'month' and request.json['n'] == 14:
        d = human_month[request.json['n']]
        print({'n': d, 'units': 'month', 'type': 'dog'})
        return {'n': d, 'units': 'month', 'type': 'dog'}
    elif request.json['type'] == 'human' and request.json['units'] == 'years' and request.json['n'] <= 9:
        d = human_month[request.json['n']]
        print({'n': d, 'units': 'month', 'type': 'dog'})
        return {'n': d, 'units': 'month', 'type': 'dog'}


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)