import json
import os

def load_dishes(file_path="data/plats.json"):
    """Charge le catalogue de plats depuis le fichier JSON."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")
        
    with open(file_path, "r", encoding="utf-8") as file:
        dishes = json.load(file)
    return dishes

# Petit test rapide
if __name__ == "__main__":
    plats = load_dishes()
    print(f"✅ {len(plats)} plats chargés avec succès !")
    print(f"Exemple de premier plat : {plats[0]['nom']}")