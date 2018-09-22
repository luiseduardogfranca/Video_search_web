from flask import Flask
from . import routes

app = Flask(__name__)
app.register_blueprint(routes.bp)

if __name__ == "__main__":
    app.run(debug=True)
