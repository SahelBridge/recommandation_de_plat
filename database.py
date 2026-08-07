from pymongo import MongoClient #mongoclient permet a py de se connecté a mongodb

# Connexion à MongoDB

client = MongoClient("mongodb://localhost:27017/")

db = client["recommendation"]

collection = db["users"] #base de donné

def save_user_profile(user_name: str, preferences: list) -> bool:


    try:

        collection.update_one(

            {"user_name": user_name},   # Recherche l'utilisateur

            {

                "$set": {

                    "preferences": preferences

                }

            },

            upsert=True   # Crée le document si l'utilisateur n'existe pas

        )

        return True

    except Exception as e:

        print("Erreur :", e)

        return False

def get_user_profile(user_name: str) -> list:


    user = collection.find_one({"user_name": user_name})

    if user:

        return user["preferences"]

    return [] 
