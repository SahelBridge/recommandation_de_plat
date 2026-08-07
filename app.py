import streamlit as st
from load_data import load_dishes, get_all_ingredients, get_all_tags, get_all_regimes
from recommendation import get_recommendations
from database import save_user_profile, get_user_profile, is_db_connected

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Système de Suggestion de Plats",
    page_icon="🍽️",
    layout="wide"
)

# Chargement du catalogue de plats (généré automatiquement si manquant)
dishes = load_dishes()
all_ingredients = get_all_ingredients(dishes)
all_tags = get_all_tags(dishes)
all_regimes = get_all_regimes(dishes)

# En-tête et Titre
st.title("🍽️ Système de Suggestion de Plats")
st.write("Trouvez les meilleurs plats adaptés à vos goûts et régimes grâce à l'IA !")

# Indication statut de la base de données
db_status = is_db_connected()
if db_status:
    st.sidebar.success("🟢 MongoDB : Connecté")
else:
    st.sidebar.info("ℹ️ MongoDB : Non connecté (mode local)")

st.sidebar.markdown("---")
st.sidebar.write(f"📊 Catalogue : **{len(dishes)}** plats enregistrés")

# Nom de l'utilisateur & Chargement Profil
col_user, col_btn = st.columns([3, 1])
with col_user:
    nom_utilisateur = st.text_input("Veuillez saisir votre nom :", placeholder="Ex: Kira")

saved_prefs = []
if nom_utilisateur.strip() and db_status:
    saved_prefs = get_user_profile(nom_utilisateur.strip())
    if saved_prefs:
        st.info(f"Profil trouvé pour **{nom_utilisateur}** : Preferences enregistrées ({', '.join(saved_prefs)})")

# Formulaire de choix des préférences
st.subheader("🎯 Vos Préférences")

default_ing = [i for i in saved_prefs if i in all_ingredients]
default_tags = [t for t in saved_prefs if t in all_tags]
default_reg = [r for r in saved_prefs if r in all_regimes]

ingredients_choisis = st.multiselect("Choisissez vos ingrédients préférés :", all_ingredients, default=default_ing)
tags_choisis = st.multiselect("Choisissez vos tags / styles :", all_tags, default=default_tags)
regimes_choisis = st.multiselect("Vos régimes alimentaires :", all_regimes, default=default_reg)

# Combinaison des préférences
user_preferences = ingredients_choisis + tags_choisis + regimes_choisis

# Bouton de validation
if st.button("🚀 Valider et recommander des plats"):
    if not nom_utilisateur.strip():
        st.warning("⚠️ Veuillez saisir un nom d'utilisateur valide.")
    elif not user_preferences:
        st.warning("⚠️ Veuillez sélectionner au moins une préférence (ingrédient, tag ou régime).")
    else:
        # Enregistrement dans MongoDB
        if db_status:
            if save_user_profile(nom_utilisateur.strip(), user_preferences):
                st.success("✅ Préférences sauvegardées dans la base de données MongoDB !")
            else:
                st.warning("⚠️ Impossible de sauvegarder dans MongoDB.")
        
        st.success("Formulaire validé ! Recherche des suggestions en cours...")
        st.divider()

        # Calcul des recommandations via le Modèle 2 (TF-IDF + Similarité Cosinus)
        recommandations = get_recommendations(user_preferences, dishes, top_n=3)

        if recommandations:
            st.subheader("⭐ Vos 3 meilleures recommandations :")
            cols = st.columns(len(recommandations))

            for idx, item in enumerate(recommandations):
                plat = item["plat"]
                score_str = item["score"]
                with cols[idx]:
                    st.markdown(f"### {idx + 1}. {plat['nom']}")
                    st.caption(f"🎯 **Score : {score_str}**")
                    st.write("**Ingrédients :**", ", ".join(plat["ingredients"]))
                    st.write("**Tags :**", ", ".join(plat["tags"]))
                    st.write("**Régimes :**", ", ".join(plat["regimes"]))
        else:
            st.info("Aucun plat ne correspond exactement à vos critères.")
