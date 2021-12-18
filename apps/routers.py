from .auth.views import auth_bp
from .spa.views import spa_bp

def init_app(app):
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(spa_bp, url_prefix='/spa')