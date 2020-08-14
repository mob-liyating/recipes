from flask import Flask, jsonify, make_response
from flask_restful import Api
from src.database import init_db, db
from src.apis.recipesApi import RecipeListAPI, RecipeAPI

import sys


def create_app():

    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    init_db(app)

    api = Api(app)
    api.add_resource(RecipeListAPI, '/recipes')
    api.add_resource(RecipeAPI, '/recipes/<int:id>')

    return app


app = create_app()


@app.before_first_request
def init():
    try: 
        db.create_all()
    except Exception as e:
        sys.stdout.write("\r Error on line {}----{}----{}".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e))
        sys.exit()


# 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
