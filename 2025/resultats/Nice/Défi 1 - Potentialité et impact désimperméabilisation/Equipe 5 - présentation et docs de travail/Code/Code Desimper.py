# ==============================================================
#  Script ultra robuste - Détection des zones désimperméabilisables
#  Auteur : ChatGPT (GPT-5) pour Ronald - 2025
# ==============================================================

import os
from qgis.core import (
    QgsProject, QgsVectorLayer, QgsRasterLayer,
    QgsField, QgsVectorFileWriter
)
from qgis.PyQt.QtCore import QVariant
import processing

print("🚀 Démarrage du script de désimperméabilisation...")

# --------------------------------------------------------------
# 1️⃣ Définition du dossier de travail
# --------------------------------------------------------------
base_path = r"C:\Users\ronal\OneDrive\Bureau\ETUDE\Master HYDROPOTECH\HACKATON"

layers = {
    "zone_etude": "St_Laurent_et_Nice.shp",
    "zone_imper1": "Zone_imper1.shp",
    "zone_imper2": "Zone_imper2.shp",
    "zone_imper3": "Zone_imper3.shp",
    "zone_imper4": "Zone_imper4.shp",
    "vege_dense": "Vege_dense.shp",
    "culture": "Culture.shp",
    "foret_faible": "Foret Faible.shp",
    "foret_dense2": "Foret Dense2.shp",
    "trottoir": "Trottoir  Commune.shp",
    "aeroport": "Aeroport.shp",
    "batiment": "Batiment.shp",
    "zone_humide": "zone_humide.shp",
    "argiles": "argiles Nice.shp",
    "mnt": "MNT.tif"
}

# --------------------------------------------------------------
# 2️⃣ Fonctions utilitaires
# --------------------------------------------------------------
def safe_path(name):
    return os.path.join(base_path, name)

def load_vector(name):
    path = safe_path(layers[name])
    if not os.path.exists(path):
        print(f"⚠️ Couche manquante : {path}")
        return None
    layer = QgsVectorLayer(path, name, "ogr")
    if not layer.isValid():
        print(f"⚠️ Erreur de chargement : {path}")
        return None
    return layer

def load_raster(name):
    path = safe_path(layers[name])
    if not os.path.exists(path):
        raise Exception(f"❌ Raster introuvable : {path}")
    layer = QgsRasterLayer(path, name)
    if not layer.isValid():
        raise Exception(f"❌ Raster invalide : {path}")
    return layer

def clean_geometry(layer):
    """Répare, simplifie et filtre les géométries invalides."""
    if not layer:
        return None
    print(f"🧹 Nettoyage géométrie : {layer.name()}")

    fixed = processing.run("native:fixgeometries", {
        'INPUT': layer,
        'OUTPUT': 'memory:'
    })['OUTPUT']

    single = processing.run("native:multiparttosingleparts", {
        'INPUT': fixed,
        'OUTPUT': 'memory:'
    })['OUTPUT']

    valid = processing.run("native:extractbyexpression", {
        'INPUT': single,
        'EXPRESSION': 'is_valid($geometry)',
        'OUTPUT': 'memory:'
    })['OUTPUT']

    return valid

# --------------------------------------------------------------
# 3️⃣ Chargement et nettoyage des couches
# --------------------------------------------------------------
zone_etude = clean_geometry(load_vector("zone_etude"))
mnt = load_raster("mnt")

imper_layers = []
for i in range(1, 5):
    lyr = clean_geometry(load_vector(f"zone_imper{i}"))
    if lyr: imper_layers.append(lyr)

if not imper_layers:
    raise Exception("❌ Aucune couche de zone imperméable valide trouvée.")

imper_fusion = processing.run("native:mergevectorlayers", {
    'LAYERS': imper_layers,
    'CRS': zone_etude.crs(),
    'OUTPUT': 'memory:'
})['OUTPUT']

non_desimper_layers = []
for x in ["vege_dense", "culture", "foret_faible", "foret_dense2", "aeroport", "zone_humide", "batiment"]:
    lyr = clean_geometry(load_vector(x))
    if lyr: non_desimper_layers.append(lyr)

non_desimper_fusion = None
if non_desimper_layers:
    non_desimper_fusion = processing.run("native:mergevectorlayers", {
        'LAYERS': non_desimper_layers,
        'CRS': zone_etude.crs(),
        'OUTPUT': 'memory:'
    })['OUTPUT']

# --------------------------------------------------------------
# 4️⃣ Calcul de la pente depuis le MNT
# --------------------------------------------------------------
slope_path = safe_path("slope_temp.tif")

print("📈 Calcul de la pente moyenne...")
processing.run("native:slope", {
    'INPUT': mnt,
    'Z_FACTOR': 1.0,
    'OUTPUT': slope_path
})

slope = QgsRasterLayer(slope_path, "Pente")
if not slope.isValid():
    raise Exception("❌ Erreur : raster de pente non valide.")

# --------------------------------------------------------------
# 5️⃣ Conversion des trottoirs (ligne → polygone)
# --------------------------------------------------------------
trottoir = clean_geometry(load_vector("trottoir"))
trottoir_poly = None
if trottoir:
    trottoir_poly = processing.run("native:buffer", {
        'INPUT': trottoir,
        'DISTANCE': 1,
        'SEGMENTS': 5,
        'END_CAP_STYLE': 0,
        'JOIN_STYLE': 0,
        'MITER_LIMIT': 2,
        'DISSOLVE': True,
        'OUTPUT': 'memory:'
    })['OUTPUT']

# --------------------------------------------------------------
# 6️⃣ Fusion trottoirs + zones imperméables
# --------------------------------------------------------------
merge_layers = [imper_fusion]
if trottoir_poly:
    merge_layers.append(trottoir_poly)

zones_pot = processing.run("native:mergevectorlayers", {
    'LAYERS': merge_layers,
    'CRS': zone_etude.crs(),
    'OUTPUT': 'memory:'
})['OUTPUT']

zones_pot = processing.run("native:clip", {
    'INPUT': zones_pot,
    'OVERLAY': zone_etude,
    'IGNORE_INVALID': True,
    'INVALID_OUTPUT': 1,
    'OUTPUT': 'memory:'
})['OUTPUT']

# --------------------------------------------------------------
# 7️⃣ Exclusion des zones interdites
# --------------------------------------------------------------
zones_ok = zones_pot
if non_desimper_fusion:
    zones_ok = processing.run("native:difference", {
        'INPUT': zones_pot,
        'OVERLAY': non_desimper_fusion,
        'IGNORE_INVALID': True,
        'INVALID_OUTPUT': 1,
        'OUTPUT': 'memory:'
    })['OUTPUT']

# --------------------------------------------------------------
# 8️⃣ Gestion de la couche des argiles
# --------------------------------------------------------------
argiles = clean_geometry(load_vector("argiles"))
if argiles:
    argiles_moyen = processing.run("native:extractbyexpression", {
        'INPUT': argiles,
        'EXPRESSION': "\"alea\" = 'Moyen'",
        'OUTPUT': 'memory:'
    })['OUTPUT']

    argiles_fortes = processing.run("native:extractbyexpression", {
        'INPUT': argiles,
        'EXPRESSION': "\"alea\" = 'Fort'",
        'OUTPUT': 'memory:'
    })['OUTPUT']

    zones_ok = processing.run("native:difference", {
        'INPUT': zones_ok,
        'OVERLAY': argiles_fortes,
        'IGNORE_INVALID': True,
        'INVALID_OUTPUT': 1,
        'OUTPUT': 'memory:'
    })['OUTPUT']

    zones_ok = processing.run("native:mergevectorlayers", {
        'LAYERS': [zones_ok, argiles_moyen],
        'CRS': zone_etude.crs(),
        'OUTPUT': 'memory:'
    })['OUTPUT']

# --------------------------------------------------------------
# 9️⃣ Statistiques de pente (exclure >10 %)
# --------------------------------------------------------------
zones_pente = processing.run("native:zonalstatisticsfb", {
    'INPUT': zones_ok,
    'INPUT_RASTER': slope,
    'RASTER_BAND': 1,
    'STATISTICS': [2],  # moyenne
    'OUTPUT': 'memory:'
})['OUTPUT']

zones_final = processing.run("native:extractbyexpression", {
    'INPUT': zones_pente,
    'EXPRESSION': '"mean" <= 10',
    'OUTPUT': 'memory:'
})['OUTPUT']

# --------------------------------------------------------------
# 🔟 Ajout d’attributs et calculs
# --------------------------------------------------------------
zones_final.startEditing()
for name, typ in [("desimper", QVariant.String),
                  ("surface", QVariant.Double),
                  ("pente", QVariant.Double),
                  ("route", QVariant.String)]:
    zones_final.addAttribute(QgsField(name, typ))
zones_final.updateFields()

trot_geoms = [f.geometry() for f in trottoir_poly.getFeatures()] if trottoir_poly else []

for f in zones_final.getFeatures():
    g = f.geometry()
    f["surface"] = g.area()
    f["pente"] = f["mean"]
    f["route"] = "Oui" if any(tg.intersects(g) for tg in trot_geoms) else "Non"
    f["desimper"] = "Oui"
    zones_final.updateFeature(f)
zones_final.commitChanges()

# --------------------------------------------------------------
# 11️⃣ Ajouter zones vides = désimper possibles
# --------------------------------------------------------------
zones_vides = processing.run("native:difference", {
    'INPUT': zone_etude,
    'OVERLAY': non_desimper_fusion if non_desimper_fusion else zone_etude,
    'IGNORE_INVALID': True,
    'INVALID_OUTPUT': 1,
    'OUTPUT': 'memory:'
})['OUTPUT']

# --------------------------------------------------------------
# 12️⃣ Fusion finale et sauvegarde
# --------------------------------------------------------------
zones_result = processing.run("native:mergevectorlayers", {
    'LAYERS': [zones_final, zones_vides],
    'CRS': zone_etude.crs(),
    'OUTPUT': 'memory:'
})['OUTPUT']

output_path = safe_path("localisation_zones_desimper.shp")
QgsVectorFileWriter.writeAsVectorFormat(
    zones_result, output_path, "utf-8", driverName="ESRI Shapefile"
)
QgsProject.instance().addMapLayer(zones_result)

print(f"✅ Résultat enregistré : {output_path}")

# --------------------------------------------------------------
# 13️⃣ Nettoyage
# --------------------------------------------------------------
if os.path.exists(slope_path):
    os.remove(slope_path)
print("🧹 Fichier temporaire supprimé.")
print("🎯 Script terminé sans erreur.")
