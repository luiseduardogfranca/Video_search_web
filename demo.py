from flask import Flask
from app.routes import bp

STATIC_FOLDER = './app/static'
TEMPLATE_FOLDER = './app/templates/'

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
