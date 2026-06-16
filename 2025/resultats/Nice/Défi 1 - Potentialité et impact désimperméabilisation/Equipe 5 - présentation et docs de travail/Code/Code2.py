import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# --- Fonction utilitaire pour afficher une image (optionnelle) ---
def afficher_image(nom_fichier):
    """Affiche une image du dossier si elle existe."""
    try:
        img = mpimg.imread(nom_fichier)
        plt.imshow(img)
        plt.axis('off')
        plt.title(nom_fichier.split('.')[0].replace('_', ' ').title())
        plt.show()
    except FileNotFoundError:
        print(f"⚠️ Image '{nom_fichier}' introuvable dans le dossier du script.")

# --- Fonctions utilitaires ---
def demander_float(message):
    """Demande à l'utilisateur un nombre et gère les erreurs."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("⚠️ Veuillez entrer une valeur numérique valide.")

def demander_choix(message, options):
    """Demande un choix parmi une liste d'options autorisées."""
    while True:
        reponse = input(message).lower().strip()
        if reponse in options:
            return reponse
        print(f"⚠️ Choix invalide. Options possibles : {', '.join(options)}")

# --- Fonctions principales par type de zone ---
def route():
    print("\n🚧 === Étude de la zone : Route ===")
    zone_economique = demander_choix("La route se situe-t-elle dans une zone économique ? (oui/non) : ", ["oui", "non"])
    if zone_economique == "oui":
        print("❌ Impossible de faire un semis ici (zone économique).")
        return

    pente = demander_float("Quelle est la pente de la route (%) ? : ")
    if pente > 10:
        print("❌ Pente trop élevée, impossible de continuer.")
        return

    nappe = demander_float("Profondeur de la nappe (en mètres) : ")
    if nappe < 3:
        print("❌ Nappe trop proche, impossible de continuer.")
        return

    revetement = demander_choix("Peut-on mettre un revêtement perméable ? (oui/non) : ", ["oui", "non"])
    if revetement == "oui":
        print("✅ Vous pouvez mettre un revêtement perméable.")
        afficher_image("revetement_permeable.jpg")
    else:
        print("❌ Vous ne pouvez pas mettre de revêtement perméable.")

def zone_pietonne():
    print("\n🚶 === Étude de la zone : Zone piétonne ===")
    pente = demander_float("Quelle est la pente de la zone piétonne (%) ? : ")
    if pente > 10:
        print("❌ Pente trop élevée, impossible.")
        return

    choix = demander_choix(
        "Voulez-vous installer une chaussée drainante ou un jardin de pluie ? (chaussee/jardin) : ",
        ["chaussee", "jardin"]
    )
    print(f"✅ Vous pouvez installer une {choix}.")
    afficher_image(f"{choix}_de_pluie.jpg" if choix == "jardin" else "chaussee_drainante.jpg")

def toiture():
    print("\n🏠 === Étude de la zone : Toiture ===")
    fondation = demander_choix("Les fondations peuvent-elles accepter la charge ? (oui/non) : ", ["oui", "non"])
    if fondation == "non":
        print("❌ Impossible de supporter la charge supplémentaire.")
        print("💡 Recommandation : installer des bassins d'infiltration ou des jardins de pluie.")
        print("🌿 Choisir des plantes nécessitant très peu d’eau.")
        afficher_image("bassin_infiltration.jpg")
        afficher_image("jardin_de_pluie.jpg")
    else:
        print("✅ Vous pouvez poursuivre avec des jardins de pluie ou un revêtement perméable.")
        afficher_image("revetement_permeable.jpg")

def parking():
    print("\n🅿️ === Étude de la zone : Parking ===")
    type_vehicule = demander_choix("Type de véhicule (velo/voiture/camion) : ", ["velo", "voiture", "camion"])
    if type_vehicule == "camion":
        print("❌ Impossible : charge trop élevée pour une surface drainante.")
        return

    pente = demander_float("Quelle est la pente du parking (%) ? : ")
    if pente > 10:
        print("❌ Pente trop élevée, impossible.")
        return

    choix = demander_choix("Voulez-vous installer des dalles drainantes ou des drains ? (dalles/drains) : ", ["dalles", "drains"])
    print(f"✅ Vous pouvez installer des {choix}.")
    afficher_image(f"{choix}.jpg")

def entrepot():
    print("\n🏭 === Étude de la zone : Entrepôt de stockage ===")
    risque_pollution = demander_choix("Risque de pollution par hydrocarbures ? (oui/non) : ", ["oui", "non"])
    if risque_pollution == "oui":
        print("❌ Risque trop élevé, installation impossible.")
        return

    nappe = demander_float("Profondeur de la nappe (en mètres) : ")
    if nappe < 3:
        print("❌ Nappe trop proche, impossible.")
        return

    pente = demander_float("Quelle est la pente (%) ? : ")
    if pente > 10:
        print("❌ Pente trop élevée, impossible.")
        return

    choix = demander_choix(
        "Voulez-vous installer des jardins de pluie ou des revêtements perméables ? (jardin/revetement) : ",
        ["jardin", "revetement"]
    )
    print(f"✅ Vous pouvez installer un {choix}.")
    afficher_image("jardin_de_pluie.jpg" if choix == "jardin" else "revetement_permeable.jpg")

# --- Programme principal ---
def main():
    print("\n🌿 === Évaluation de faisabilité environnementale ===\n")
    zone = demander_choix(
        "La zone est-elle une route, une zone piétonne, une toiture, un parking ou un entrepôt de stockage ? : ",
        ["route", "zone piétonne", "toiture", "parking", "entrepôt de stockage"]
    )

    if zone == "route":
        route()
    elif zone == "zone piétonne":
        zone_pietonne()
    elif zone == "toiture":
        toiture()
    elif zone == "parking":
        parking()
    elif zone == "entrepôt de stockage":
        entrepot()

if __name__ == "__main__":
    main()
