from flask import Blueprint, jsonify

shares_bp = Blueprint('shares',__name__)

@shares_bp.route('/')
def shares_index():
    return "shares"