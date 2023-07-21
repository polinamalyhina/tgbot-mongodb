import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["testeclipsebd"]
idea_collection = db["users_ideas"]


def useridea(user_idea, username, user_id):
    """
    Save user idea into DB to read it later
    """
    post = {"username": username, "user_id": user_id, "user_idea": user_idea}
    idea_collection.insert_one(post)
