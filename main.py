from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api')
def my_microservice():
    response = jsonify({'Hello': 'World!'})
    return response


@app.route('/api/person/<id>')
def person(id):
    response = jsonify({'Hello': id})
    return response


if __name__ == '__main__':
    print(app.url_map)
    app.run()
