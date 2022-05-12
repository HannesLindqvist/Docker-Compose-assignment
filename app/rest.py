import mysql.connector
from flask import Flask, request, jsonify, Response
from flaskext.mysql import MySQL


app = Flask(__name__)

mydb = mysql.connector.connect(
       host="db",
       user="root",
       password="root",
       database="HannesDB"
        )



@app.route('/persons', methods=['POST'])
def post_route():
  
    data = request.get_json()
    cursor = mydb.cursor()
    request.method == 'POST'
    name = data['name']
    last_name = data['last_name']

    cursor.execute('INSERT INTO user(name, last_name) VALUES (%s, %s)', (name, last_name))
    mydb.commit()


    return Response("", status=200, mimetype='application/json')


@app.route('/persons', methods=['GET'])
def get_route():

    cursor = mydb.cursor()
    request.method == 'GET'

    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    resp = jsonify(rows)

    return resp



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
