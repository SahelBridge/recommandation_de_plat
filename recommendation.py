from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from load_data import load_dishes

def get_recommendations(preferences, dishes=None, top_n=3):
    """
    Calcule les recommandations de plats en utilisant TF-IDF et la similarité cosinus (Modèle 2).
    
    :param preferences: Liste des préférences utilisateur (ingrédients, tags, régimes)
    :param dishes: Liste des plats (si None, chargés depuis data/plats.json)
    :param top_n: Nombre de plats à recommander
    :return: Liste de dictionnaires contenant le plat, le score brut et le score en %
    """
    if dishes is None:
        dishes = load_dishes()

    if not preferences or not dishes:
        return []

    # 1. Transformer chaque plat en document texte
    documents = []
    for plat in dishes:
        texte = (
            plat["nom"] + " "
            + " ".join(plat["ingredients"]) + " "
            + " ".join(plat["tags"]) + " "
            + " ".join(plat["regimes"])
        )
        documents.append(texte)

    # 2. Vectorisation TF-IDF
    vectorizer = TfidfVectorizer()
    matrice_plats = vectorizer.fit_transform(documents)

    # 3. Vectorisation des préférences utilisateur
    texte_preferences = " ".join(preferences)
    vecteur_preferences = vectorizer.transform([texte_preferences])

    # 4. Calcul de la similarité cosinus
    similarites = cosine_similarity(vecteur_preferences, matrice_plats)[0]

    # 5. Association score <-> plat
    resultats = []
    for i, plat in enumerate(dishes):
        score_val = float(similarites[i])
        score_pct = round(score_val * 100, 1)
        
        resultats.append({
            "plat": plat,
            "nom": plat["nom"],
            "ingredients": plat["ingredients"],
            "tags": plat["tags"],
            "regimes": plat["regimes"],
            "score_val": score_val,
            "score": f"{score_pct}% de correspondance"
        })

    # 6. Tri décroissant par score
    resultats.sort(key=lambda x: x["score_val"], reverse=True)

    # 7. Retourner le Top N
    return resultats[:top_n]

if __name__ == "__main__":
    test_prefs = ["poisson", "epice", "halal"]
    print(f"🔍 Test de recommandation (TF-IDF / Modèle 2) pour les préférences : {test_prefs}\n")
    recs = get_recommendations(test_prefs)
    print("Top des recommandations :")
    for idx, r in enumerate(recs, 1):
        print(f"{idx}. {r['nom']} -> Score : {r['score']} ({r['score_val']:.4f})")
