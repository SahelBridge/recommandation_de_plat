from pymongo import MongoClient
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError

# Connexion à MongoDB avec un délai d'attente court (2 secondes max si DB non lancée)
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    db = client["recommendation"]
    collection = db["users"]
except Exception as e:
    client = None
    db = None
    collection = None

def save_user_profile(user_name: str, preferences: list) -> bool:
    """Sauvegarde ou met à jour le profil utilisateur dans MongoDB."""
    if collection is None:
        print("⚠️ MongoDB indisponible. Impossible d'enregistrer le profil.")
        return False
    try:
        collection.update_one(
            {"user_name": user_name},
            {"$set": {"preferences": preferences}},
            upsert=True
        )
        return True
    except (PyMongoError, ServerSelectionTimeoutError) as e:
        print("Erreur d'accès MongoDB :", e)
        return False

def get_user_profile(user_name: str) -> list:
    """Récupère les préférences enregistrées de l'utilisateur."""
    if collection is None:
        return []
    try:
        user = collection.find_one({"user_name": user_name})
        if user:
            return user.get("preferences", [])
    except (PyMongoError, ServerSelectionTimeoutError) as e:
        print("Erreur d'accès MongoDB :", e)
    return []

def is_db_connected() -> bool:
    """Vérifie si la connexion à MongoDB est fonctionnelle."""
    if client is None:
        return False
    try:
        client.admin.command('ping')
        return True
    except Exception:
        return False
