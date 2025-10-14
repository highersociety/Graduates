from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)
    
    # Configure CORS
    CORS(app, origins=[app.config['FRONTEND_URL']])
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.clubs import clubs_bp
    from routes.events import events_bp
    from routes.admin import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(clubs_bp, url_prefix='/api/clubs')
    app.register_blueprint(events_bp, url_prefix='/api/events')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Health check endpoint
    @app.route('/api/health')
    def health_check():
        return {'status': 'healthy', 'message': 'CEMS API is running'}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)