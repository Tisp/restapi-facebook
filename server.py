from flask import Flask, jsonify, make_response, request
from lib.database import User, FacebookUsers
from lib import facebook_api

server = Flask(__name__)
fb_users = FacebookUsers()

@server.route('/person/', methods=['GET'])
def get_users():
    
    limit  = request.args.get('limit')
    if not limit:
        limit = None

    users = fb_users.get_all(limit)
    output = []

    for user in users:
        output.append({
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'gender': user.gender
        })

    return make_response(jsonify(output), 200)
        
@server.route('/person/<int:id>', methods=['DELETE'])
def rm_user(id):
    rm = fb_users.remove(id)
    #Usuario nao encontrado
    if not rm:
        return make_response(jsonify({'error': 'User not found'}), 500)

    return make_response('', 204)

@server.route('/person/', methods=['POST'])
def add_user():
    id = request.form['facebookId']
    try:
        user_data = facebook_api.get_user_info(id)
        user_name = user_data['username'] if 'username' in user_data else ''
        gender = user_data['gender'] if 'gender' in user_data else ''
        new_user = User(id=user_data['id'], name=user_data['name'], username=user_name, gender=gender)
        fb_users.add(new_user)
        return make_response('', 201)
    except Exception as e:
        return make_response(jsonify({'error': e}), 500)



@server.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)    
    


if __name__ == '__main__':
    server.run(debug=True)
