from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hasjdhaskjdksahajsdashk'


    from .monitoring import monitoring_bp
    app.register_blueprint(monitoring_bp)

    from .dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp,url_prefix="/dashboard/")

    from .shares import shares_bp
    app.register_blueprint(shares_bp,url_prefix="/shares/")

    from .portfolio import portfolio_bp
    app.register_blueprint(portfolio_bp,url_prefix="/portfolio/")


    return app