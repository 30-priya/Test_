from functools import wraps
from flask import request, jsonify
from src.models.user import User, RoleEnum
from flask_jwt_extended import jwt_required, get_jwt_identity

def check_role_permission(*allowed_roles):
    def decorator(func):
        @wraps(func)
        @jwt_required() 
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            
            user = User.query.filter_by(id=current_user['id']).first()
            
            if user.role.value in allowed_roles:
                return func(*args, **kwargs)
            else:
                return jsonify({"message": "Unauthorized"}), 401
        return wrapper
    return decorator
