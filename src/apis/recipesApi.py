from flask import abort, jsonify, make_response, request
from flask_restful import Resource, reqparse
from src.models.recipes import RecipesModel, RecipesSchema
from src.database import db


class RecipeListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
            help = 'No title provided', location = 'json')
        self.reqparse.add_argument('making_time', type = str, required = True,
            help = 'No making_time provided', location = 'json')
        self.reqparse.add_argument('serves', type = str, required = True,
            help = 'No serves provided', location = 'json')
        self.reqparse.add_argument('ingredients', type = str, required = True,
            help = 'No ingredients provided', location = 'json')
        self.reqparse.add_argument('cost', type = int, required = True,
            help = 'No cost provided', location = 'json')
        super(RecipeListAPI, self).__init__()

    def get(self):
        results = RecipesModel.query.all()
        res = RecipesSchema(many=True).dump(results).data
        return make_response(jsonify({
                'recipes': res
            }), 200)
    
    def post(self):
        args = self.reqparse.parse_args()
        recipe = RecipesModel(args.title, args.making_time, args.serves, args.ingredients, args.cost)

        try:
            db.session.add(recipe)
        except:
            db.session.rollback()
            return make_response(jsonify({
                'message': 'Recipe creation failed!',
                "required": "title, making_time, serves, ingredients, cost"
                }), 400)
        else:
            db.session.commit()
            res = RecipesSchema().dump(recipe).data
            return make_response(jsonify({
                'message': 'Recipe successfully created!',
                'recipe': res
                }), 201)


class RecipeAPI(Resource):
    def get(self, id):
        if not id:
            recipe_id = 1
        try:
            recipe_id = int(id)
        except:
            abort(404)
        
        result = db.session.query(RecipesModel).filter_by(id=recipe_id).first()
        res = RecipesSchema().dump(result).data

        return make_response(jsonify({
                'message': 'Recipe details by id',
                'recipe': res
                }), 200)

    def put(self, id):
        if not id:
            recipe_id = 1
        try:
            recipe_id = int(id)
        except:
            abort(404)
        
        recipe = db.session.query(RecipesModel).filter_by(id=recipe_id).first()
        if recipe == None:
            abort(404)
        args = self.reqparse.parse_args()
        for name, value in args.items():
            if value is not None:
                setattr(recipe, name, value)
        db.session.add(recipe)
        db.session.commit()
        return make_response(jsonify({
                'message': 'Recipe successfully updated!'
                }), 204)

    def delete(self, id):
        if not id:
            recipe_id = 1
        try:
            recipe_id = int(id)
        except:
            abort(404)

        recipe = db.session.query(RecipesModel).filter_by(id=recipe_id).first()
        if recipe is not None:
            db.session.delete(recipe)
            db.session.commit()
            return make_response(jsonify({
                'message': 'Recipe successfully removed!'
                }), 204)
        else 
            return make_response(jsonify({
                'message': 'No Recipe found!'
                }), 400)