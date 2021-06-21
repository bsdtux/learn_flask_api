from flask import Blueprint
from flask_restful import Api
from resources.courses import Course, CourseList
from resources.reviews import Review, ReviewList

api_bp = Blueprint("api", __name__)
api = Api(api_bp)


# Route
api.add_resource(CourseList, "/courses")
api.add_resource(Course, "/course/<string:course_id>")
api.add_resource(ReviewList, "/reviews")
api.add_resource(Review, "/review/<string:review_id>")
