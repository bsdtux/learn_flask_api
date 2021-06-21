from flask import jsonify
from flask_restful import Resource, reqparse


class CourseList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", required=True, help="No course title provided", location=["form", "json"])
        self.reqparse.add_argument("url", required=True, help="No course url provided", location=["form", "json"])

    def get(self):
        return jsonify(dict(courses=[dict(title="Python Basics")]))


class Course(Resource):
    def get(self, course_id):
        return jsonify(dict(title="Python Basics"))

    def put(self, course_id):
        return jsonify(dict(title="Python Basics"))

    def delete(self, course_id):
        return jsonify(dict(title="Python Basics"))
