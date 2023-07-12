from flask import Blueprint, jsonify

monitoring_bp = Blueprint('monitoring',__name__)

@monitoring_bp.route('/')
def index():
    return "Hello World"

@monitoring_bp.route('/hello')
def hello():
    return "Hello World hello"

@monitoring_bp.route('/hello/<name>')
def hello_name(name):
    return f"Hello World {name}"

