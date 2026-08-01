def calculer_score(preferences_utilisateur, plat):

    score = 0

    ingredients = plat["ingredients"]
    tags = plat["tags"]
    regimes = plat["regimes"]

    for preference in preferences_utilisateur:

        if preference in ingredients:
            score = score + 2

        if preference in tags:
            score = score + 1

        if preference in regimes:
            score = score + 3

    return score


def trier_recommandations(plats_scores):

    n = len(plats_scores)

    for i in range(n):

        for j in range(0, n - i - 1):

            if plats_scores[j]["score"] < plats_scores[j + 1]["score"]:

                temp = plats_scores[j]
                plats_scores[j] = plats_scores[j + 1]
                plats_scores[j + 1] = temp

    return plats_scores


def get_recommendations(preferences_utilisateur, liste_plats):

    resultats = []

    for plat in liste_plats:

        score = calculer_score(preferences_utilisateur, plat)

        resultats.append({
            "score": score,
            "plat": plat
        })

    resultats_tries = trier_recommandations(resultats)

    top_3 = []

    compteur = 0

    for element in resultats_tries:

        if compteur < 3:
            top_3.append(element["plat"])
            compteur = compteur + 1

    return top_3

if __name__ == "__main__":

    dishes = [
        {
            "id": "plat_01",
            "nom": "Tchep au poisson",
            "ingredients": ["riz", "poisson", "carotte"],
            "tags": ["epice", "plat_chaud"],
            "regimes": ["halal"]
        },
        {
            "id": "plat_02",
            "nom": "Salade composée",
            "ingredients": ["laitue", "tomate", "concombre"],
            "tags": ["leger", "frais"],
            "regimes": ["vegetarien", "halal"]
        },
        {
            "id": "plat_03",
            "nom": "Poulet braisé",
            "ingredients": ["poulet", "oignon"],
            "tags": ["grillade"],
            "regimes": ["halal"]
        }
    ]

    preferences = ["halal", "poisson", "epice"]

    recommendations = get_recommendations(preferences, dishes)

    print("Top 3 des recommandations :")
    for dish in recommendations:
        print("-", dish["nom"])

        