from flask import request, jsonify, Blueprint
from src.models.Items import Item
from src.common.database import Database
from src.common.utils import check_role_permission
list_items_blueprint = Blueprint("list_items", __name__) 
@list_items_blueprint.route("/list_items", methods=["GET"])
@check_role_permission('Role1', 'Role2', 'Role3')
def list_items():
    try:
        items = Item.query.all()
        item_list = []
        for item in items:
            item_data = {
                "id": item.id,
                "name": item.name,
                "description": item.description,
            }
            item_list.append(item_data)
        return jsonify(items=item_list), 200

    except Exception as e:
        return jsonify(message=f"Error in listing items: {e}"), 400
