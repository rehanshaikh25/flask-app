from flask import Blueprint, jsonify

info_bp = Blueprint('info', __name__)

@info_bp.route('/info')
def info():
    app_info = {
        "App_name": "Python/Flask App",
        "Description": "This is a simple Python/Flask app made using the App-Factory pattern.",
        "Status": "running"
    }
    return jsonify(app_info)
