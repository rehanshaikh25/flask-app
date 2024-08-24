from flask import Blueprint, jsonify
from ..models import User  # Ensure this import is correct and not causing issues

members_bp = Blueprint('members', __name__)

@members_bp.route('/members')
def members():
    users = User.query.all()
    members_info = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(members_info)
