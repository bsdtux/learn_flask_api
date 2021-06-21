from flask import jsonify
from flask_restful import Resource


class ReviewList(Resource):
    def get(self):
        return jsonify({"reviews": [dict(course=1, rating=5)]})


class Review(Resource):
    def get(self, review_id):
        return jsonify(dict(course=1, rating=5))

    def put(self, review_id):
        return jsonify(dict(course=1, rating=5))

    def delete(self, review_id):
        return jsonify(dict(course=1, rating=5))
