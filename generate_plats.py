import json
import random
import os

# 1. Base de données élargie (720 combinaisons uniques possibles)
bases_plats = [
    {"nom": "Tchep", "genre": "M", "ing_base": ["riz", "tomate", "oignon"], "tags": ["dejeuner", "traditionnel"]},
    {"nom": "Yassa", "genre": "M", "ing_base": ["oignon", "citron", "moutarde", "riz"], "tags": ["dejeuner", "diner"]},
    {"nom": "Maffe", "genre": "M", "ing_base": ["pate_d_arachide", "tomate", "riz"], "tags": ["dejeuner", "riche"]},
    {"nom": "Riz Gras", "genre": "M", "ing_base": ["riz", "tomate", "oignon", "poivron"], "tags": ["dejeuner"]},
    {"nom": "Alloco", "genre": "M", "ing_base": ["banane_aloco", "huile", "piment"], "tags": ["diner", "friture", "fast_food"]},
    {"nom": "Salade", "genre": "F", "ing_base": ["laitue", "tomate", "concombre"], "tags": ["entree", "frais", "leger"]},
    {"nom": "Soupe", "genre": "F", "ing_base": ["bouillon", "oignon", "ail", "persil"], "tags": ["diner", "chaud", "leger"]},
    {"nom": "Grillade", "genre": "F", "ing_base": ["oignon", "piment", "citron"], "tags": ["diner", "grillade"]},
    {"nom": "Sauté", "genre": "M", "ing_base": ["sauce_soja", "poivron", "carotte", "riz"], "tags": ["dejeuner", "asiatique"]},
    {"nom": "Lasagne", "genre": "F", "ing_base": ["pates", "tomate", "fromage", "oignon"], "tags": ["diner", "italien"]},
    {"nom": "Brochette", "genre": "F", "ing_base": ["oignon", "poivron", "epices"], "tags": ["grillade", "fast_food"]},
    {"nom": "Couscous", "genre": "M", "ing_base": ["semoule", "carotte", "courgette", "pois_chiches"], "tags": ["traditionnel", "dejeuner"]},
    {"nom": "Bowl", "genre": "M", "ing_base": ["quinoa", "avocat", "maïs", "concombre"], "tags": ["frais", "healthy"]},
    {"nom": "Curry", "genre": "M", "ing_base": ["lait_de_coco", "curry", "oignon", "riz"], "tags": ["epice", "chaud"]},
    {"nom": "Wok", "genre": "M", "ing_base": ["nouilles", "poivron", "champignons", "sauce_soja"], "tags": ["asiatique", "rapide"]}
]

proteines = [
    {"nom": "au Poulet", "ing": "poulet"},
    {"nom": "au Boeuf", "ing": "boeuf"},
    {"nom": "au Poisson", "ing": "poisson"},
    {"nom": "aux Crevettes", "ing": "crevettes"},
    {"nom": "d'Agneau", "ing": "agneau"},
    {"nom": "au Tofu", "ing": "tofu"},
    {"nom": "aux Légumes", "ing": "courgette"},
    {"nom": "aux Oeufs", "ing": "oeuf"}
]

variations = [
    {"nom_m": "Épicé", "nom_f": "Épicée", "tag": "epice", "ing": "piment"},
    {"nom_m": "Doux", "nom_f": "Douce", "tag": "doux", "ing": "herbes_de_provence"},
    {"nom_m": "Royal", "nom_f": "Royale", "tag": "fete", "ing": "champignons"},
    {"nom_m": "Maison", "nom_f": "Maison", "tag": "familial", "ing": "pomme_de_terre"},
    {"nom_m": "Express", "nom_f": "Express", "tag": "rapide", "ing": "mais"},
    {"nom_m": "Gourmand", "nom_f": "Gourmande", "tag": "riche", "ing": "creme_fraiche"}
]

# 2. Listes de filtrage pour déterminer les régimes réels
VIANDES_POISSONS = {"poulet", "boeuf", "poisson", "crevettes", "agneau"}
PRODUITS_ANIMAUX = VIANDES_POISSONS.union({"fromage", "oeuf", "creme_fraiche", "bouillon"})
GLUTEN = {"pates", "semoule", "nouilles"}

def determiner_regimes(ingredients):
    ing_set = set(ingredients)
    regimes = ["halal"]
    
    # Végétarien (aucune viande ni poisson)
    if not ing_set.intersection(VIANDES_POISSONS):
        regimes.append("vegetarien")
        
    # Vegan (aucun produit d'origine animale)
    if not ing_set.intersection(PRODUITS_ANIMAUX):
        regimes.append("vegan")
        
    # Sans Gluten
    if not ing_set.intersection(GLUTEN):
        regimes.append("sans-gluten")
        
    return regimes

# 3. Génération des 500 combinaisons sans doublons ni boucle infinie
toutes_combinaisons = []
for base in bases_plats:
    for prot in proteines:
        for var in variations:
            toutes_combinaisons.append((base, prot, var))

random.shuffle(toutes_combinaisons)

plats = []
for count, (base, prot, var) in enumerate(toutes_combinaisons[:500], start=1):
    adj = var["nom_f"] if base["genre"] == "F" else var["nom_m"]
    nom_plat = f"{base['nom']} {prot['nom']} {adj}"
    
    ingredients = list(set(base["ing_base"] + [prot["ing"], var["ing"]]))
    tags = list(set(base["tags"] + [var["tag"]]))
    regimes = determiner_regimes(ingredients)
    
    plat = {
        "id": f"plat_{count:03d}",
        "nom": nom_plat,
        "ingredients": ingredients,
        "tags": tags,
        "regimes": regimes
    }
    plats.append(plat)

# 4. Sauvegarde dans data/plats.json
os.makedirs("data", exist_ok=True)
chemin_fichier = os.path.join("data", "plats.json")

with open(chemin_fichier, "w", encoding="utf-8") as f:
    json.dump(plats, f, ensure_ascii=False, indent=2)

print(f"🎉 Succès ! Le fichier '{chemin_fichier}' a été généré avec {len(plats)} plats !")
