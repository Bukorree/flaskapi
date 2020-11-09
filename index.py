from flask import Flask, escape, request, jsonify
import pandas as pd
import string
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def Home():
    a = request.args.get('name')
    b = request.args.get('date')
    data = pd.read_json('stock_price_data.json')
    # print(data)
    dicdata = data[[a]].tail(int(b)).to_dict(orient="index")
    z=[dicdata[i] for i in dicdata]
    day = [i for i in dicdata]
    print(day)
    day = [str(i)[:10] for i in day]
    print(day)
    print(list(map(lambda x:x[a],z)))
    dicpass = dict(zip(day,list(map(lambda x:x[a],z))))
    print(dicpass)
    # print(data[[a]].tail(int(b)).to_dict(orient="index"))
    # return jsonify(data[[a]].tail(int(b)).to_dict())
    return jsonify(dicpass)




if __name__ == "__main__":
    app.run(debug=True)
