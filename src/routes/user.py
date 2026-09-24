from flask import Blueprint, jsonify, request
from src.supabase_client import supabase

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = supabase.table('user').select('*').execute().data
    return jsonify(users)

@user_bp.route('/users', methods=['POST'])
def create_user():
    
    data = request.json
    user = supabase.table('user').insert({'username': data['username'], 'email': data['email']}).execute().data[0]
    return jsonify(user), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = supabase.table('user').select('*').eq('id', user_id).limit(1).execute().data
    if not users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users[0])

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    changes = {key: data[key] for key in ('username', 'email') if key in data}
    if not changes:
        return get_user(user_id)
    users = supabase.table('user').update(changes).eq('id', user_id).execute().data
    if not users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users[0])

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = supabase.table('user').delete().eq('id', user_id).execute().data
    if not users:
        return jsonify({'error': 'User not found'}), 404
    return '', 204
