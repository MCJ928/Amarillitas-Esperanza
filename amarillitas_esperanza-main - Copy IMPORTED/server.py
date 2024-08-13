from flask_app import app

from flask_app.controller import companies_controller, users_controller, products_controller

if __name__ == "__main__":
    app.run(debug=True)