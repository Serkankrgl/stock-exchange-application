from flask import Blueprint, jsonify

dashboard_bp = Blueprint('dashboard',__name__)

@dashboard_bp.route('/')
def dashboard_index():
    return "dashboard"