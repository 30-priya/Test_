from flask import request, jsonify, Blueprint
from src.models.Items import Item
from src.models.user import User
from src.common.database import Database
from src.common.utils import check_role_permission
from flask_jwt_extended import jwt_required


create_item_blueprint = Blueprint("create_item", __name__)   
@create_item_blueprint.route("/items", methods=["POST"])
@check_role_permission('Role2', 'Role3')
@jwt_required()
def create_item():
    try:
        data = request.get_json(force=True)
        name = data['name']
        description = data['description']
        user = User.query.filter_by().first()
        if user.role == 'Role2':
            item = Item(name=name, description=description)
            Database.db.session.add(item)
            Database.db.session.commit()

            return jsonify(message="Item created successfully"), 201

        elif user.role == 'Role3':
            print("XCVBNCVBN")
            item = Item(name=name, description=description)
            Database.db.session.add(item)
            Database.db.session.commit()

            return jsonify(message="Item created successfully"), 201

        else:
            # Unauthorized role
            return jsonify(message="Unauthorized"), 401

    except Exception as e:
        return jsonify(message=f"Error in creating item: {e}"), 400