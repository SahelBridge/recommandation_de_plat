import streamlit as st
st.set_page_config(layout="wide")#Pti ajout pour que l'affichage s'adapte mieux à l'ecran

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
if st.button("Valider les préférences"):
    if not nom_utilisateur.strip(): #.strip pour que ça refuse aussi quand il met espace 
        st.warning("Veuillez saisir un nom valide")
    elif not user_preferences:
        st.warning("Veuillez selectionner vos preferences")
    else:
        st.success("Formulaire validé ! Recherche de suggestion en cours...")
        st.divider()  # Ligne de séparation visuelle
        
        # Données de test en attendant recommendation.py(les vraies données)
        top_3_plats = [
            {
                "nom": "Tchep au poisson",
                "ingredients": ["riz", "poisson", "carotte"],
                "regimes": ["halal"],
                "score": "95% de correspondance"
            },
            {
                "nom": "Salade Composée",
                "ingredients": ["laitue", "tomate", "oeuf", "concombre"],
                "regimes": ["vegetarien", "sans-gluten"],
                "score": "88% de correspondance"
            },
            {
                "nom": "Poulet Yassa",
                "ingredients": ["riz", "oignon"],
                "regimes": ["halal"],
                "score": "82% de correspondance"
            }
        ]
        # Affichage du Top 3 côte à côte dans 3 colonnes
        st.subheader(" Vos 3 meilleures recommandations :")
        col1, col2, col3 = st.columns(3)#Creation de 3 colonnes independantes et de meme tailles

        # Colonne 1 : Plat 1
        with col1:
            st.markdown(f"### 1-{top_3_plats[0]['nom']}")#Texte en gras avec ### pour rendre ça plus gros
            st.caption(f" {top_3_plats[0]['score']}")#Texte un peu plus discret pour donner des details par exemple
            st.write("**Ingrédients :**", ", ".join(top_3_plats[0]['ingredients']))#le join c'est pour que ça s'affiche plus joliment
            st.write("**Régimes :**", ", ".join(top_3_plats[0]['regimes']))

        # Colonne 2 : Plat 2
        with col2:
            st.markdown(f"### 2-{top_3_plats[1]['nom']}")
            st.caption(f"{top_3_plats[1]['score']}")
            st.write("**Ingrédients :**", ",".join(top_3_plats[1]['ingredients']))
            st.write("**Régimes :**",",".join(top_3_plats[1]['regimes']))

        # Colonne 3 : Plat 3
        with col3:
           st.markdown(f" ### 3-{top_3_plats[2]['nom']}")
           st.caption(f"{top_3_plats[2]['score']}")
           st.write("**Ingrédients :**",",".join(top_3_plats[2]['ingredients']))
           st.write("**Régimes :**",",".join(top_3_plats[2]))
