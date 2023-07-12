from flask import Blueprint, jsonify

portfolio_bp = Blueprint('portfolio',__name__)

@portfolio_bp.route('/')
def portfolio_index():
    return "portfolio"