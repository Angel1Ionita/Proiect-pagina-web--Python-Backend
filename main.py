import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
from flask import abort

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False
data = json.load(open("db.json"))

@app.route('/table',methods=['GET'])
def get_table():
    list=jsonify(data['table'])
    return list

@app.route('/piese',methods=['GET'])
def get_piese():
    list=jsonify(data['piese'])
    return list

@app.route('/ceasuri',methods=['GET'])
def get_ceasuri():
    list=jsonify(data['ceasuri'])
    return list

@app.route('/comanda',methods=['GET'])
def get_comanda():
    list=jsonify(data['comanda'])
    return list

@app.route('/comanda',methods=['POST'])
def post_comanda():
    body = request.json
    list=data['comanda']
    if body not in list:
        list.append(body)
    else:
        abort(404)
    data['comanda']=list
    jsonfile=data
    with open('db.json','w') as f:
        json.dump(jsonfile,f,indent=4)
    return "<h1>Produsul a fost adaugat in cos !<h1>"

@app.route('/comanda/<id>',methods=['PUT'])
def put_comanda(id):
    body = request.json
    list=data['comanda']
    for element in list:
        if element['id']==int(id) and element['cantitate']>0:
            element['cantitate']=body['cantitate']
            break
    data['comanda']=list
    jsonfile=data
    with open('db.json','w') as f:
        json.dump(jsonfile,f,indent=4)
    return "<h1>Produs modificat !<h1>"

@app.route('/comanda/<id>',methods=['DELETE'])
def delete_comanda(id):
    list=data['comanda']
    for element in list:
        if element['id']==int(id):
            list.remove(element)
            break
    data['comanda']=list
    jsonfile=data
    with open('db.json','w') as f:
        json.dump(jsonfile,f,indent=4)
    return "<h1>Produsul a fost sters din cos !<h1>"

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Error 404 Not Found<h1>",404

app.run(host='localhost',port=3000)
