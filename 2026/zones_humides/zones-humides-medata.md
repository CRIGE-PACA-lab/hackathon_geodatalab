# 🗺️ Zones humides 

Deux jeux de données sont disponibles dans ce geopackage : 

1. [Jeu de données « Zones humides » — RPDZH / Géosource (Forum des Marais Atlantiques)](## Couche 'export_zh_reseau_zones_humides')
2. [Jeu de données « Zones humides » — DDTM 13 (Bouches-du-Rhône)](## Couche 'export_zone_humide_ddtm13')


## Couche 'export_zh_reseau_zones_humides'

> **Réseau Partenarial des Données sur les Zones Humides (RPDZH)** · Forum des Marais Atlantiques

La donnée géographique multipartenariale **« zones humides »** présente un **inventaire (non exhaustif)** des zones humides effectives, c'est-à-dire des zones identifiées et délimitées **après inventaire de terrain**. Elle est alimentée en continu par les membres et partenaires du réseau (structures locales en charge des inventaires) : plus de **155 inventaires partenaires** et plus de **2 000 000 ha** de zones humides référencés.

---

### 📌 Identité du jeu de données


| Élément                              | Valeur                                                                                                                                             |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Titre**                            | Zones humides                                                                                                                                      |
| **Catalogue**                        | [Géosource – RPDZH](http://www.geosource.reseau-zones-humides.org/geosource/srv/fre/catalog.search#/metadata/cceb45a0-67a7-46a9-a20c-ee90b581789d) |
| **Catégorie**                        | Environnement                                                                                                                                      |
| **Mots-clés**                        | Hydrographie · zones humides · marais · inventaires · Environnement                                                                                |
| **Langue**                           | Français                                                                                                                                           |
| **Type de ressource**                | Jeu de données (vecteur, GeoPackage)                                                                                                               |
| **Date de création**                 | 2010-01-01                                                                                                                                         |
| **Date de révision**                 | 2025-02-20                                                                                                                                         |
| **Dernière mise à jour de la fiche** | avril 2026                                                                                                                                         |
| **Étendue spatiale**                 | France (hors bassin Rhône-Méditerranée-Corse pour certains inventaires)                                                                            |


### 👥 Contacts &amp; conditions
                                     
**Distributeur**  : Forum Marais Atlantiques  [fma@forum-marais-atl.com](mailto:fma@forum-marais-atl.com) 


### 🔗 Accès à la donnée


| Ressource                                       | Lien                                                                                                                                                    |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cartographie RPDZH (visualiseur SIG)**        | [http://sig.reseau-zones-humides.org/](http://sig.reseau-zones-humides.org/)                                                                            |
| **Téléchargement « zones humides effectives »** | Via la [fiche Géosource](http://www.geosource.reseau-zones-humides.org/geosource/srv/fre/catalog.search#/metadata/cceb45a0-67a7-46a9-a20c-ee90b581789d) |
| **Métadonnées (XML ISO 19139)**                 | [Export XML](http://www.geosource.reseau-zones-humides.org/geosource/srv/fre/xml.metadata.get?uuid=cceb45a0-67a7-46a9-a20c-ee90b581789d)                |


### 🗂️ Contenu de la table attributaire

La couche est livrée en **GeoPackage**. Elle comporte **35 champs** décrits ci-dessous, regroupés par thématique.

#### 🆔 Identification &amp; gestion


| Champ                     | Description                                                             | Type   |
| ------------------------- | ----------------------------------------------------------------------- | ------ |
| `fid`                     | Champ automatique donné par le GeoPackage                               | Entier |
| `gid`                     | Identifiant de la zone humide (base FMA)                                | Entier |
| `zh_part_id`              | Identifiant du partenaire fournisseur                                   | Texte  |
| `id_de_l_inventaire`      | Identifiant de l'inventaire dans la base du FMA                         | Entier |
| `zhu_id_sitfonc`          | Identifiant et nom du site fonctionnel auquel appartient la zone humide | Entier |
| `libelle`                 | Nom de la zone ou du lieu-dit le plus proche et le plus important       | Texte  |
| `date_de_creation_du_mh`  | Date de création de la zone humide                                      | Texte  |
| `zh_majdate`              | Date de mise à jour de l'entité                                         | Texte  |
| `statut_du_milieu_humide` | Statut de la zone humide (**validé** ou **gelé**)                       | Texte  |


#### 📅 Inventaire


| Champ          | Description                                                                                                                | Type  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------- | ----- |
| `datecreation` | Date de création de l'inventaire                                                                                           | Texte |
| `datedebut`    | Date du début de l'inventaire                                                                                              | Texte |
| `datefin`      | Date de fin de l'inventaire                                                                                                | Texte |
| `qualif`       | Champ concaténé : nom de l'inventaire dans Gwern, nom du dossier donné à l'inventaire, nom de l'organisme saisi dans Gwern | Texte |


#### 🌿 Typologie des habitats (Corine Biotope, EUNIS, Prodrome)


| Champ              | Description                                                       | Type   |
| ------------------ | ----------------------------------------------------------------- | ------ |
| `zhu_cbi`          | Code Corine Biotope principal                                     | Texte  |
| `zhu_cbipourc`     | Pourcentage de recouvrement de l'habitat Corine Biotope principal | Entier |
| `cbi2`             | Code(s) Corine Biotope secondaires                                | Texte  |
| `zhu_eun`          | Code EUNIS principal                                              | Texte  |
| `zhu_eun_pourc`    | Pourcentage de recouvrement de l'habitat EUNIS principal          | Entier |
| `zhu_pro`          | Code Prodrome principal                                           | Texte  |
| `zhu_propourc`     | Pourcentage de recouvrement du Prodrome principal                 | Entier |
| `sag`              | Typologie SAGE                                                    | Texte  |
| `zhu_rq_typologie` | Remarque sur la typologie                                         | Texte  |


#### 🐾 Espèces observées


| Champ                  | Description                                     | Type  |
| ---------------------- | ----------------------------------------------- | ----- |
| `eve`                  | Espèces végétales observées dans la zone humide | Texte |
| `zhu_especes_animales` | Espèces animales observées dans la zone humide  | Texte |


#### 💧 Hydrologie, biologie &amp; remarques


| Champ             | Description                                      | Type  |
| ----------------- | ------------------------------------------------ | ----- |
| `zhu_rq_hydro`    | Remarque se rapportant aux données hydrologiques | Texte |
| `zhu_rq_bio`      | Remarque se rapportant aux données biologiques   | Texte |
| `zhu_rq_con`      | Remarque concernant le contexte                  | Texte |
| `zhu_rq_bilan`    | Remarque concernant le bilan                     | Texte |
| `zhu_rq_generale` | Remarque générale                                | Texte |
| `zhu_observateur` | Nom de l'observateur de terrain                  | Texte |


#### ⚖️ Enjeux réglementaires &amp; gestion


| Champ                | Description                                                                                                                                           | Type    |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `zhu_propo_zhiep`    | Zone Humide d'Intérêt Environnemental Particulier (**ZHIEP**) : impliquant la mise en place d'un programme d'actions                                  | Texte   |
| `zhu_propo_zsge`     | Zone Stratégique pour la Gestion de l'Eau (**ZSGE**), à l'intérieur des ZHIEP : impliquant la mise en place d'un programme d'actions et de servitudes | Booléen |
| `zhu_recommandation` | Recommandations techniques de mise en œuvre des actions                                                                                               | Booléen |


#### 📐 Caractéristiques spatiales


| Champ        | Description                                                               | Type      |
| ------------ | ------------------------------------------------------------------------- | --------- |
| `surfcal_ha` | Surface de la zone humide (hectares)                                      | Numérique |
| `type_imb`   | Type d'imbication : **10 = marais**, **40 = ZHE** (zone humide effective) | Texte     |


---

## Couche 'export_zone_humide_ddtm13'

> **Direction Départementale des Territoires et de la Mer des Bouches-du-Rhône (DDTM 13)** · Pôle SIG et Analyse Territoriale

Inventaire des zones humides du département établi par le **CEN PACA** (Conservatoire d'espaces naturels Provence-Alpes-Côte d'Azur) en **juillet 2019** a permis de recueillir les données offrant une approche globale de l'état de ces milieux.


### 📌 Identité du jeu de données

| Élément | Valeur |
|---|---|
| **Titre** | Les zones humides sur le département des Bouches-du-Rhône |
| **Page data.gouv** | [Les zones humides sur le département des Bouches-du-Rhône](https://www.data.gouv.fr/datasets/les-zones-humides-sur-le-departement-des-bouches-du-rhone) |
| **Fiche d'origine (catalogue Geo-IDE)** | [catalogue.geo-ide.developpement-durable.gouv.fr](http://catalogue.geo-ide.developpement-durable.gouv.fr/catalogue/srv/fre/catalog.search#/metadata/fr-120066022-jdd-9962e585-3e84-4fd7-8168-a42be83994ef) |
| **Diffuseur / producteur** | DDTM 13 (Pôle SIG et Analyse Territoriale) |
| **Mots-clés (tags)** | cen · données-ouvertes · eau-zonages-eau · hydrographie · inspire · zh · zone-humide |
| **Résolution spatiale** | 1/25 000 |
| **Étendue spatiale** | Département des Bouches-du-Rhône (environ 4,23° E – 5,81° E / 43,16° N – 43,92° N) |
| **Publication sur data.gouv** | 12 février 2021 |
| **Dernière mise à jour** | 10 septembre 2026 |
| **Licence** | Licence Ouverte / Open Licence version 2.0 |

### ⚖️ Cadre réglementaire et méthodologique

- **Définition légale** (art. L. 211-1 du Code de l'environnement) : « on entend par zone humide les terrains, exploités ou non, habituellement inondés ou gorgés d'eau douce, salée ou saumâtre de façon permanente ou temporaire, ou dont la végétation, quand elle existe, y est dominée par des plantes hygrophiles pendant au moins une partie de l'année ».
- **Critères de délimitation** : l'arrêté du 24 juin 2008 précise les critères de définition et de délimitation (art. L. 214-7-1 et R. 211-108). Une zone est considérée comme humide si elle présente au moins l'un des critères suivants :
  - ses sols correspondent à un ou plusieurs types pédologiques mentionnés à l'annexe 1 dudit arrêté ;
  - sa végétation, si elle existe, est caractérisée par des espèces indicatrices de zones humides ou par des habitats caractéristiques de zones humides.
- **Typologie** : le MNHN a élaboré en 1996 une typologie nationale (13 catégories), reprise dans le **SDAGE Rhône-Méditerranée** et précisée dans le Guide technique SDAGE n°5. Chaque zone humide inventoriée est caractérisée par un « type SDAGE ».


### 🗂️ Contenu de la table attributaire

#### 🆔 Identification

| Champ | Description | Type | Exemple |
|---|---|---|---|
| `id_0` | Identifiant interne (GeoPackage/PostGIS) | Entier | `22` |
| `id` / `id_map` | Identifiant de la zone humide | Entier | `101` |
| `id_sandre` | Identifiant Sandre (« NR » si non renseigné) | Texte | `NR` |
| `id_local` | Identifiant local de l'inventaire | Texte | `13CEN0079` |
| `structure` | Structure productrice de la donnée | Texte | `CEN PACA` |
| `nom` | Nom de la zone humide | Texte | `Canal des Garrigues et d'Alleins` |
| `date_` | Date d'inventaire | Texte (JJ/MM/AAAA) | `09/08/2017` |
| `obs` | Observateur de terrain | Texte | `E.OULES` |
| `cod_ssbv` | Code du sous-bassin versant | Texte | `DU_13_09` |
| `coord_x` / `coord_y` | Coordonnées du centroïde (Lambert-93) | Numérique | `867005.43 / 6289877.63` |

#### 🌿 Typologie & caractéristiques

| Champ | Description | Type | Exemple |
|---|---|---|---|
| `typo_sdage` | Code du type SDAGE (cf. tableau des 10 types) | Entier | `5` |
| `type_sdage` | Libellé du type SDAGE | Texte | `bordures de cours d'eau` |
| `surface` | Surface de la zone humide (hectares) | Numérique | `31.09` |
| `statu` | Statut de la zone (score) | Numérique | `0` |

##### Les dix types principaux de zones humides dans les Bouches-du-Rhône

| Code | Type SDAGE |
|---|---|
| 2 | Baies et estuaires moyens-plats |
| 3 | Marais et lagunes côtiers |
| 4 | Marais saumâtres aménagés |
| 5 | Bordures de cours d'eau |
| 6 | Plaines alluviales |
| 9 | Petits plans d'eau et bordures de plans d'eau |
| 10 | Marais et landes humides de plaine et de plateau |
| 11 | Zones humides ponctuelles |
| 12 | Marais aménagés dans un but agricole |
| 13 | Zones humides artificielles |

#### ⭐ Évaluation — valeur patrimoniale & fonctions (scores 0–100)

| Champ | Description | Exemple |
|---|---|---|
| `note_glob` | Note globale d'évaluation de la zone humide | `50,5` |
| `valpatri` | Valeur patrimoniale globale | `68,8` |
| `valpatrbio` | Valeur patrimoniale biologique | `29` |
| `habpatri` | Habitats patrimoniaux | `13` |
| `florepatri` | Flore patrimoniale | `14` |
| `vertpatri` | Vertébrés patrimoniaux | `1` |
| `invertpatr` | Invertébrés patrimoniaux | `1` |
| `fcthydro` | Fonctions hydrologiques | `65` |
| `fcteco` | Fonctions écologiques | `100` |
| `protphys` | Protection physique du milieu | `25` |
| `epur` | Fonction d'épuration | `25` |
| `valsoeco` | Valeur socio-économique | `100` |
| `loispeda` | Loisirs et pédagogie | `50` |
| `prod` | Production (valorisation agricole…) | `50` |
| `stgs` | Score global « statut » | `50` |
| `stnnatetg` | État naturel / état général de la station | `15` |
| `etfctl` | État fonctionnel de la zone | `10` |
| `typesdage` | Score du type SDAGE | `50` |
| `priointerv` | Priorité d'intervention | `20` |
| `gestcons` | Gestion conservatoire | `50` |
| `hydro` | Note hydrologique | `0` |
| `bio` | Note biologique | `10` |
| `mnc` | Menaces et pressions | `0` |

#### 🎯 Décision de gestion

| Champ | Description | Type | Exemple |
|---|---|---|---|
| `decision` | Décision de gestion issue de l'évaluation | Texte | `VEILLE` |

### 📜 Conditions d'utilisation

- **Licence Ouverte / Open Licence version 2.0** ([texte de la licence](https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf)) ;
- Utilisation libre **sous réserve de citer la DDTM 13 comme source de données et d'indiquer la date de mise à jour** ;
- Pas de restriction d'accès public selon INSPIRE ;
- Aucun des articles de la loi ne peut être invoqué pour justifier d'une restriction d'accès public.


## ⚠️ Avertissement

Ces données proviennent de sources multiples : inventaires locaux de zones humides, numérisation à partir d'orthophotoplans (BD ORTHO® IGN) ou fonds topographiques (Scan25® IGN), périmètres d'Unités Hydrauliques Cohérentes ou de syndicats de marais, inventaires floristiques/faunistiques, et données mises à disposition par les partenaires du RPDZH. Les échelles d'exploitation varient du **1/5 000ᵉ au 1/100 000ᵉ** selon la provenance.

Il s'agit de données **sans prétention d'exhaustivité**, qui ne constituent **en aucun cas un outil réglementaire**. Les utilisateurs exploitent les données sous leur responsabilité, sans recours possible contre le partenaire fournisseur.

---

*Fiche établie d'après la métadonnée ISO 19115/19139 publiée sur le catalogue Géosource du RPDZH et le dictionnaire des champs fourni par le producteur.*