#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
 
app.config['MONGODB_SETTINGS'] = {
    'db': 'mongodb',
    'user' : 'mongo',
    'password' :'BURA5605FUmEMhCXtkkv' ,
    'host': 'containers-us-west-27.railway.app',
    'port': 7720
}
db = MongoEngine()
db.init_app(app)
@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅 API"})


# class User(db.Document):
#     name = db.StringField()
#     email = db.StringField()
#     def to_json(self):
#         return {"name": self.name,
#                 "email": self.email}

# @app.route('/', methods=['GET'])
# def query_records():
#     name = request.args.get('name')
#     user = User.objects(name=name).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         return jsonify(user.to_json())

# @app.route('/', methods=['PUT'])
# def create_record():
#     record = json.loads(request.data)
#     user = User(name=record['name'],
#                 email=record['email'])
#     user.save()
#     return jsonify(user.to_json())

# @app.route('/', methods=['POST'])
# def update_record():
#     record = json.loads(request.data)
#     user = User.objects(name=record['name']).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         user.update(email=record['email'])
#     return jsonify(user.to_json())
