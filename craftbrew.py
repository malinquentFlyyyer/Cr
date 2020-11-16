from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

import craft_brews 


app = Flask(__name__)
api = Api(app)

class Brews(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(craft_brews.bar_order), 200
        for brew in craft_brews.bar_order:
            if (brew["id"] == id):
                return brew, 200

        return "Quote not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("craft")
        parser.add_argument("brand")
        parser.add_argument("location")
        params = parser.parse_args()

        for brew in craft_brews.bar_order:
            if(id == brew["id"]):
                return f"Craft brew with id {id} already exists in brewery directory", 400

        brew = {
            "id": int(id),
            "craft": params["craft"],
            "brand": params["brand"],
            "location": params["location"]
            }

        craft_brews.append(brew)
        return brew, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("craft")
        parser.add_argument("brand")
        parser.add_argument("location")
        params = parser.parse_args()
        
        for brew in craft_brew.bar_order:
            if(id == brew["id"] ):
                brew["craft"] = params["craft"]
                brew["brand"] = params["brand"]
                brew["location"] = params["location"]
                return brew, 200

        brew = {
            "id": id,
            "craft": params["craft"],
            "brand": params["brand"],
            "location": params["location"]
            }

        craft_brews.bar_order.append(brew)
        return brew, 201


    def delete(self, id):
        global bar_order
        craft_brews.bar_order = [brew for brew in craft_brew.bar_order if brew["id"] != id]
        return f"Brew with id {id} is deleted from the brewery.", 200
    
api.add_resource(Brews, "/craft-brews", "/craft-brews/", "/craft-brews/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
        


