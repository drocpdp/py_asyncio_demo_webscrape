from flask import Flask

app = Flask(__name__)

# Blueprints
from webscrape.views import main_bp

app.register_blueprint(main_bp)