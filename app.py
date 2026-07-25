import streamlit as st

#Titre
st.title("Système de Suggestion de Plats")
st.write("Bienvenue sur notre appli")

#Nom de l'utilisateur
nom_utilisateur= st.text_input("Veuillez saisir votre nom :",placeholder="Ex:Kira")

#Liste des options
ingredients=["riz", "poisson", "carotte", "chou", "oignon", "laitue", "tomate", "concombre", "maïs", "oeuf"]
tags=["dejeuner", "epice", "plat_chaud", "entree", "frais", "leger"]
regimes=["halal","vegetarien","sans-gluten"]

#Choix
ingredients_choisis=st.multiselect("Choisissez vos ingrédients:",ingredients)
tags_choisis=st.multiselect("Choisissez vos tags:",tags)
regimes_choisis=st.multiselect("Vos régimes alimentaires:",regimes)

#Combinaison
user_preferences=ingredients_choisis+tags_choisis+regimes_choisis

#Les conditions 
if st.button:
    if not nom_utilisateur.strip(): #.strip pour que ça refuse aussi quand il met espace 
        st.warning("Veuillez saisir un nom valide")
    elif not user_preferences:
        st.warning("Veuillez selectionner vos preferences")
    else:
        st.success("Formulaire validé ! Recherche de suggestion en cours...")
        #A rendre plus joli plutard--st.write("Voici vos preferences:",user_preferences)
