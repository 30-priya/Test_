from src.models.user import User, RoleEnum
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import re
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Blueprint, request, jsonify
from src.common.database import Database
import datetime
user_blueprint = Blueprint("user", __name__)   
@user_blueprint.route("/create-user", methods=["POST"])  
def create_user():
    try:
        data = request.get_json(force=True)
        username= data['username']
        email=data['email']  
        password=data['password']  
        role = data['Role'] 
        # allowed_roles = [role.value for role in RoleEnum]
        # if role not in allowed_roles:
        #     print("2222")
        #     return jsonify(message="Invalid role"), 400
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        user_check = User.query.filter_by(email=email).first()
        print(user_check)
        if not user_check :
            if(re.fullmatch(regex,email)) :
                if ((len(password)>=8 )) and  re.search("[a-z]",password) and re.search("[0-9]",password) and   re.search("[A-Z]",password) and re.search("[$#@]",password):
                    db_user = User(username=username,email=email,role=role,password=generate_password_hash(password))
                    Database.db.session.add(db_user)
                    Database.db.session.commit()
                    
                    return {'message':"Successfully created"}, 201
                else:
                    return jsonify(message= "Invalid Password, Minimum length 8 character, password must have special character ,Upper case,Lower case and digits"),400
            else:
                return jsonify(message="Invalid Email Format"),400  
        else:
            return jsonify(message="Email Already Exists"),404
    except Exception as e:
        return jsonify(message=f"Error in creating User = {e}"),400
    
