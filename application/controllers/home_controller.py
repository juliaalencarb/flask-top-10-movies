from flask import Flask, render_template, make_response
from flask_restx import Namespace, Resource
from application.database import database_service

api = Namespace('home', description='Loads all movies onto homepage.')
db = database_service.instance


@api.route("/")
class HomePage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("index.html"), 200, headers)
