import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# 1. CHARGER LES PLATS
# ==========================================

with open("data/plats.json", "r", encoding="utf-8") as fichier:
    plats = json.load(fichier)

print("Nombre de plats :", len(plats))


# ==========================================
# 2. TRANSFORMER CHAQUE PLAT EN TEXTE
# ==========================================

documents = []

for plat in plats:

    texte = (
        plat["nom"] + " "
        + " ".join(plat["ingredients"]) + " "
        + " ".join(plat["tags"]) + " "
        + " ".join(plat["regimes"])
    )

    documents.append(texte)


# ==========================================
# 3. TRANSFORMER LES TEXTES EN VECTEURS
# ==========================================

vectorizer = TfidfVectorizer()

matrice_plats = vectorizer.fit_transform(documents)


# ==========================================
# 4. PREFERENCES DE L'UTILISATEUR
# ==========================================

preferences = ["poisson", "epice", "halal"]

texte_preferences = " ".join(preferences)


# ==========================================
# 5. TRANSFORMER LES PREFERENCES EN VECTEUR
# ==========================================

vecteur_preferences = vectorizer.transform([texte_preferences])


# ==========================================
# 6. CALCULER LA SIMILARITE
# ==========================================

similarites = cosine_similarity(
    vecteur_preferences,
    matrice_plats
)


# ==========================================
# 7. ASSOCIER CHAQUE SCORE A SON PLAT
# ==========================================

resultats = []

for i, plat in enumerate(plats):

    score = similarites[0][i]

    resultats.append({
        "plat": plat,
        "score": score
    })


# ==========================================
# 8. TRIER LES PLATS
# ==========================================

resultats.sort(
    key=lambda element: element["score"],
    reverse=True
)


# ==========================================
# 9. PRENDRE LES 3 MEILLEURS
# ==========================================

top_3 = resultats[:3]


# ==========================================
# AFFICHAGE
# ==========================================

print("Top 3 des recommandations :")

for element in top_3:

    print(
        element["plat"]["nom"],
        "-> score :",
        round(element["score"], 3)
    )