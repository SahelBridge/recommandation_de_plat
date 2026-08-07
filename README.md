# 🍽️ Système de Recommandation de Plats

Application Python et Streamlit pour la recommandation de plats basée sur l'intelligence artificielle (vectorisation TF-IDF et similarité cosinus).

---

## 🗂️ Architecture et Connexion des Fichiers

L'application est structurée de manière modulaire, où chaque composant communique avec les autres :

```
recommandation_de_plat/
├── data/
│   └── plats.json         # Base de données JSON (500 plats générés)
├── generate_plats.py      # Générateur de données de plats synthétiques
├── load_data.py           # Chargement des données & extraction des ingrédients/tags/régimes
├── recommendation.py      # Moteur de recommandation (TF-IDF & Cosine Similarity - Modèle 2)
├── database.py            # Gestion du stockage MongoDB (profils et préférences utilisateurs)
├── app.py                 # Interface utilisateur interactive (Streamlit)
└── README.md
```

### 🔗 Flux d'exécution et Interconnexion :
1. **`generate_plats.py`** : Génère 500 plats variés avec ingrédients, tags et régimes alimentaires (halal, végétarien, vegan, sans-gluten).
2. **`load_data.py`** : Charge `data/plats.json` (le génère automatiquement via `generate_plats.py` s'il est absent) et fournit les helpers d'extraction.
3. **`recommendation.py`** : Reçoit les préférences utilisateur de `app.py`, vectorise les textes des plats via `scikit-learn` (TF-IDF) et calcule la similarité cosinus pour retourner le Top 3.
4. **`database.py`** : (Optionnel) Enregistre et récupère le profil utilisateur dans MongoDB.
5. **`app.py`** : Interface Web Streamlit reliant tous les modules pour une expérience utilisateur fluide.

---

## 🚀 Lancement de l'application

### 1. Lancer l'interface Web (Streamlit)
```bash
streamlit run app.py
```

### 2. Tester le moteur de recommandation seul (CLI)
```bash
python3 recommendation.py
```

### 3. Régénérer les plats
```bash
python3 generate_plats.py
```