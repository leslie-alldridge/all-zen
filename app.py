from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

tickets = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]


class User(Resource):
    def get(self, name):
        for ticket in tickets:
            if(name == ticket["name"]):
                return ticket, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for ticket in tickets:
            if(name == ticket["name"]):
                return "ticket with name {} already exists".format(name), 400

        ticket = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(ticket)
        return ticket, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for ticket in tickets:
            if(name == ticket["name"]):
                ticket["age"] = args["age"]
                ticket["occupation"] = args["occupation"]
                return ticket, 200

        ticket = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        tickets.append(ticket)
        return ticket, 201

    def delete(self, name):
        global tickets
        tickets = [ticket for ticket in tickets if ticket["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
