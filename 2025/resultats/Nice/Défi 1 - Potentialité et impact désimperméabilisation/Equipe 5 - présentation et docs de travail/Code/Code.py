def route():
    zone_economique = input("La route se situe-t-elle dans une zone économique ? (oui/non) : ").lower()
    if zone_economique == "oui":
        print("Impossible de faire un semis ici.")
        return
    pente = float(input("Quelle est la pente de la route (%) ? : "))
    if pente > 10:
        print("Pente trop élevée, impossible de continuer.")
        return
    nappe = float(input("Profondeur de la nappe (en mètres) : "))
    if nappe < 3:
        print("Nappe trop proche, impossible de continuer.")
        return
    revetement = input("Peut-on mettre un revêtement perméable ? (oui/non) : ").lower()
    if revetement == "oui":
        print("Vous pouvez mettre un revêtement perméable.")
    else:
        print("Vous ne pouvez pas mettre de revêtement perméable.")


def zone_pietonne():
    pente = float(input("Quelle est la pente de la zone piétonne (%) ? : "))
    if pente > 10:
        print("Pente trop élevée, impossible.")
        return
    choix = input("Voulez-vous installer une chaussée drainante ou un jardin de pluie ? (chaussée/jardin) : ").lower()
    if choix in ["chaussée", "jardin"]:
        print(f"Vous pouvez installer {choix}.")
    else:
        print("Choix invalide.")


def toiture():
    fondation = input("Les fondations peuvent-elles accepter la charge ? (oui/non) : ").lower()
    if fondation == "non":
        print("Impossible de déconnecter le bâtiment et mettre des bassins d'infiltration.")
        print("Si vous installez des jardins de pluie, choisissez des plantes nécessitant très peu d'eau.")
    else:
        print("Vous pouvez continuer avec l'installation de jardins de pluie ou de revêtements perméables.")


def parking():
    type_vehicule = input("Type de véhicule (velo/voiture/camion) : ").lower()
    if type_vehicule == "camion":
        print("Impossible d'installer ici.")
        return
    pente = float(input("Quelle est la pente du parking (%) ? : "))
    if pente > 10:
        print("Pente trop élevée, impossible.")
        return
    choix = input("Voulez-vous installer des dalles drainantes ou des drains ? (dalles/drains) : ").lower()
    print(f"Vous pouvez installer {choix}.")


def entrepot():
    risque_pollution = input("Risque de pollution par hydrocarbures ? (oui/non) : ").lower()
    if risque_pollution == "oui":
        print("Impossible d'installer.")
        return
    nappe = float(input("Profondeur de la nappe (en mètres) : "))
    if nappe < 3:
        print("Nappe trop proche, impossible.")
        return
    pente = float(input("Quelle est la pente (%) ? : "))
    if pente > 10:
        print("Pente trop élevée, impossible.")
        return
    choix = input("Voulez-vous installer des jardins de pluie ou des revêtements perméables ? (jardin/revetement) : ").lower()
    print(f"Vous pouvez installer {choix}.")


def main():
    zone = input("La zone est-elle une route, une zone piétonne, une toiture, un parking, ou un entrepôt de stockage ? : ").lower()
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
    else:
        print("Type de zone invalide.")


if __name__ == "__main__":
    main()
