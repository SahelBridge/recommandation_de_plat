import json
import os
from generate_plats import generate_dishes

def load_dishes(file_path="data/plats.json"):
    """Charge le catalogue de plats depuis le fichier JSON. le génère s'il n'existe pas."""
    if not os.path.exists(file_path):
        print(f"Le fichier {file_path} n'existe pas. Génération automatique...")
        return generate_dishes(file_path)
        
    with open(file_path, "r", encoding="utf-8") as file:
        dishes = json.load(file)
    return dishes

def get_all_ingredients(dishes):
    """Extrait la liste triée de tous les ingrédients uniques de la base de données."""
    ingredients = set()
    for dish in dishes:
        ingredients.update(dish.get("ingredients", []))
    return sorted(list(ingredients))

def get_all_tags(dishes):
    """Extrait la liste triée de tous les tags uniques."""
    tags = set()
    for dish in dishes:
        tags.update(dish.get("tags", []))
    return sorted(list(tags))

def get_all_regimes(dishes):
    """Extrait la liste triée de tous les régimes uniques."""
    regimes = set()
    for dish in dishes:
        regimes.update(dish.get("regimes", []))
    return sorted(list(regimes))

if __name__ == "__main__":
    plats = load_dishes()
    print(f"✅ {len(plats)} plats chargés avec succès !")
    print(f"Exemple de premier plat : {plats[0]['nom']}")
    print(f"Total ingrédients uniques : {len(get_all_ingredients(plats))}")
    print(f"Total tags uniques : {len(get_all_tags(plats))}")
    print(f"Total régimes uniques : {len(get_all_regimes(plats))}")