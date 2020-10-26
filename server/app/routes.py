from app import app
from flask import Flask, jsonify,request
from app.models import User

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            logging_in = User.authenticate(**data)

            if not logging_in:
                print("invalid user")
                return jsonify({'message':'invalid credentials','authenticated':False}),401
            print("valid")
            return jsonify({'message':'valid','authenticated':True}),200
            return "success"
