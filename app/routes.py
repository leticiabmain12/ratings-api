from app import db
from app.models.rating import Rating
from flask import Blueprint, jsonify, make_response, request

ratings_bp = Blueprint("ratings_bp",__name__, url_prefix="/ratings")

@ratings_bp.route("", methods=["POST"])
def handle_ratings():
    request_body = request.get_json()
    new_rating = Rating(
        brand_name = request_body["brand_name"],
        brand_rating = request_body["brand_rating"]
    )
    db.session.add(new_rating)
    db.session.commit()

    return f"Rating {new_rating.brand_name} created", 201


@ratings_bp.route("", methods=["GET"])
def get_ratings():
    ratings = Rating.query.all()
    ratings_response =[]
    for rating in ratings:
        ratings_response.append(
            {"name": rating.brand_name,
            "rating": rating.brand_rating})
    return jsonify(ratings_response)



@ratings_bp.route("/<brand_rating>", methods=["GET"])
def top_rating (brand_rating):
    ratings = Rating.query.filter_by(brand_rating=brand_rating)
    print(ratings)
    ratings_response =[]
    for rating in ratings:
        ratings_response.append(
            {"name": rating.brand_name,
            "rating": rating.brand_rating})
    return jsonify(ratings_response)


   




#######
####

# @ratings_bp.route("/<rating_id>", methods=["GET"])
# def handle_rating (rating_id):

#     rating= Rating.query.get(rating_id)

#     if rating == None:
#         return make_response(f"rating{rating_id}is not found", 404)
    
#     return{
#         "brand_name":rating.brand_name,
#         "brand_rating":rating.brand_rating
#     }
    

    # brand_rating = Rating.query.get(Rating.brand_rating)
    
    # rating_response = []
    # for rating in Rating.brand_rating:
    #     rating_response.append(rating.to_dict()
    #             )
    # return jsonify(rating_response)


# @ratings_bp.route("/<rating_brand_rating>", methods=["GET"])
# def handle_rating (rating_brand_rating):

#     rating= Rating.query.get(rating_brand_rating)

#     if rating == None:
#         return make_response(f"rating{rating_brand_rating}is not found", 404)
    
#     return{
#         "brand_name":rating.brand_name,
#         "brand_rating":rating.brand_rating
#    }