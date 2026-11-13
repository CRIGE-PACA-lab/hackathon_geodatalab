# Métadonnées des couches du GeoPackage « Protections environnementales en Provence-Alpes-Côte d'Azur »

Ce document rassemble les métadonnées des 11 couches du GeoPackage. Chaque section reprend les éléments de la page source du jeu de données d'origine (description, producteur, licence, date de mise à jour, lien de téléchargement) ainsi que la structure de la table attributaire (champs, libellés, types, définitions et modalités).

## Table des matières

1. [1. DH_ZSC — Sites Natura 2000 au titre de la Directive Habitats (ZSC)](#1-dh_zsc--sites-natura-2000-au-titre-de-la-directive-habitats-zsc)
2. [2. DO_ZPS — Sites Natura 2000 au titre de la Directive Oiseaux (ZPS)](#2-do_zps--sites-natura-2000-au-titre-de-la-directive-oiseaux-zps)
3. [3. DPA_P — Directive paysagère des Alpilles](#3-dpa_p--directive-paysagère-des-alpilles)
4. [4. L_SITE_INSCRIT_S_R93 — Sites inscrits](#4-l_site_inscrit_s_r93--sites-inscrits)
5. [5. N_ENP_APB_S_R93 — Arrêtés préfectoraux de protection de biotope (APPB)](#5-n_enp_apb_s_r93--arrêtés-préfectoraux-de-protection-de-biotope-appb)
6. [6. RNN — Réserves naturelles nationales](#6-rnn--réserves-naturelles-nationales)
7. [7. RNR — Réserves naturelles régionales](#7-rnr--réserves-naturelles-régionales)
8. [8. znieff1 — ZNIEFF de type I](#8-znieff1--znieff-de-type-i)
9. [9. znieff2 — ZNIEFF de type II](#9-znieff2--znieff-de-type-ii)
10. [10. cdl — Conservatoire du littoral](#10-cdl--conservatoire-du-littoral)
11. [11. cen — Conservatoires d'espaces naturels](#11-cen--conservatoires-despaces-naturels)

---

## 1. DH_ZSC — Sites Natura 2000 au titre de la Directive Habitats (ZSC)

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `DH_ZSC` |
| Titre du jeu de données source | Sites Natura 2000 au titre de la Directive Habitats en Provence-Alpes-Côte d'Azur |
| Type de donnée | Couches vectorielles (périmètres de protection réglementaire) |
| Emprise | Région Provence-Alpes-Côte d'Azur |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Le réseau Natura 2000 a pour objectif d'identifier un réseau européen représentatif et cohérent d'espaces pour y favoriser le maintien de la biodiversité, tout en tenant compte des exigences économiques, sociales, culturelles et régionales dans une logique de développement durable. Il est fondé sur deux directives européennes :

- **1979 « Directive Oiseaux »** : elle prévoit la création de « Zones de Protection Spéciale » (ZPS), afin d'assurer la conservation d'espèces d'oiseaux jugées d'intérêt communautaire.
- **1992 « Directive Habitats »** : elle prévoit la création des « Zones Spéciales de Conservation » (ZSC) destinées à permettre la conservation d'habitats et d'espèces.

Pour la Directive Habitats : les ZSC sont définies par la directive européenne du 21/05/1992 sur la conservation des habitats naturels. Un inventaire identifiant les sites (sites éligibles) susceptibles d'être proposés au réseau Natura 2000 a été initialement réalisé et agréé par le Muséum National d'Histoire Naturelle (MNHN). Les ZSC étant en cours de constitution, l'état d'avancement des sites est renseigné (pSIC/SIC/ZSC) :

- **pSIC** : site proposé par chaque État membre à la Commission Européenne pour intégrer le réseau Natura 2000 / Directive Habitats ;
- **SIC** : site sélectionné sur la base des propositions par la Commission Européenne ;
- **ZSC** : zone constitutive du réseau Natura 2000 par arrêté ministériel.

### Structure de la table attributaire

Champs de la table attributaire de la couche `DH_ZSC` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `SITECODE` | Code du site Natura 2000 | Texte | Code unique du site au niveau européen (format FR9xxxxxx). Permet le lien avec la fiche INPN. | Ex. FR9301497 |
| `SITENAME` | Nom officiel du site | Texte | Nom officiel de désignation du site (SIC/ZSC) tel que transmis à la Commission européenne. | — |
| `NOM_USUEL` | Nom usuel | Texte | Nom usuel du site utilisé par la DREAL. | — |
| `AVANCEMENT` | État d'avancement du site | Texte | État d'avancement du site dans la constitution du réseau Natura 2000 (Directive Habitats). | `ZSC` : Zone Spéciale de Conservation désignée par arrêté ministériel ; `pSIC` : site d'intérêt communautaire proposé à la Commission européenne ; `SIC` : Site d'Importance Communautaire retenu par la CE |
| `S_SIG_HA` | Surface SIG (hectares) | Réel (double) | Surface calculée sous SIG, en hectares. | — |
| `R_BIOGEO` | Région biogéographique | Texte | Région(s) biogéographique(s) de rattachement du site (directive Habitats). | `MED` : méditerranéenne ; `ALP` : alpine ; `ALP-MED` : site à cheval sur les deux régions |
| `D_PROP_CE` | Date de proposition à la CE | Date | Date de transmission du site (pSIC) à la Commission européenne. | — |
| `D_LIST_ALP` | Date d'inscription sur la liste (région alpine) | Date | Date d'inscription du site sur la liste régionale alpine transmise à la CE. | — |
| `D_LIST_MED` | Date d'inscription sur la liste (région méditerranéenne) | Date | Date d'inscription du site sur la liste régionale méditerranéenne transmise à la CE. | — |
| `D_DESIG_AM` | Date de désignation (arrêté ministériel) | Date | Date de désignation du site en ZSC par arrêté ministériel. | — |
| `DOCOB` | État d'avancement du DOCOB | Texte | État d'avancement du document d'objectifs Natura 2000. | `0_SANS DOCOB` ; `1_DOCOB EN ELABORATION` ; `2_DOCOB ACHEVE` ; `3_DOCOB EN ANIMATION` |
| `OPERATEUR` | Opérateur | Texte | Structure opératrice chargée de la rédaction du document d'objectifs. | — |
| `ANIMATEUR` | Animateur | Texte | Structure animatrice chargée de la mise en œuvre du DOCOB. | — |
| `COMMENT` | Commentaire | Texte | Remarques sur le site (historique de désignation, particularités de gestion…). | — |
| `LIEN_INV` | Liens avec inventaires | Texte | Liens avec les anciens inventaires (ZICO, propositions régionales…). | Ex. PR95, PAC25 |
| `SOURCE` | Source des données | Texte | DREAL productrice de la donnée (les sites frontaliers peuvent être gérés par la DREAL voisine). | Ex. `DREAL PACA`, `DREAL Occi` |
| `ECHEL_NUM` | Échelle de numérisation | Texte | Échelle de numérisation du périmètre. | `1/25 000`, `1/50 000`, `1/100 000` |
| `D_NUM_MAJ` | Date de dernière mise à jour de la numérisation | Date | Date de la dernière mise à jour géométrique. | — |
| `D_ATT_MAJ` | Date de dernière mise à jour des attributs | Date | Date de la dernière mise à jour des données descriptives. | — |
| `COUCHE` | Nom de la couche | Texte | Nom de la couche d'origine. | `ZSC` |
| `URL_FICHE` | URL de la fiche INPN | Texte (URL) | Lien vers la fiche du site sur l'INPN. | https://inpn.mnhn.fr/site/natura2000/… |
| `URL_DOCOB` | URL du DOCOB | Texte (URL) | Lien vers le document d'objectifs sur le SIDE PACA. | — |
| `URL_TEXTE` | URL du texte de désignation | Texte (URL) | Lien vers l'acte de désignation (pdf). | — |

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | DREAL Provence-Alpes-Côte d'Azur |
| Source (téléchargement) | <https://www.data.gouv.fr/datasets/sites-natura-2000-au-titre-de-la-directive-habitats-en-provence-alpes-cote-dazur> |
| Licence | Licence Ouverte / Open Licence version 2.0 |
| Dernière mise à jour de la source | 12 août 2026 |
| Label | INSPIRE |

---

## 2. DO_ZPS — Sites Natura 2000 au titre de la Directive Oiseaux (ZPS)

### Identification

| Nom de la couche (GeoPackage) | `DO_ZPS` |
| Titre du jeu de données source | Sites Natura 2000 au titre de la Directive Oiseaux en Provence-Alpes-Côte d'Azur |
| Type de donnée | Couches vectorielles (périmètres de protection réglementaire) |
| Emprise | Région Provence-Alpes-Côte d'Azur |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Périmètre des zones de protection spéciale (ZPS) appartenant au réseau européen Natura 2000.

Le réseau Natura 2000 comprend 2 types de zones réglementaires : les Zones de Protection Spéciale (ZPS) et les Zones Spéciales de Conservation (ZSC).

Les ZPS sont désignées à partir de l'inventaire des Zones Importantes pour la Conservation des Oiseaux (ZICO) définies par la directive européenne 79/409/CEE du 25/04/1979 concernant la conservation des oiseaux sauvages. La désignation des ZPS relève d'une décision nationale, se traduisant par un arrêté ministériel, sans nécessiter un dialogue préalable avec la Commission européenne.

### Structure de la table attributaire

Champs de la table attributaire de la couche `DO_ZPS` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `SITECODE` | Code du site Natura 2000 | Texte | Code unique du site au niveau européen (format FR9xxxxxx). | — |
| `SITENAME` | Nom officiel du site | Texte | Nom officiel de désignation de la ZPS. | — |
| `NOM_USUEL` | Nom usuel | Texte | Nom usuel du site utilisé par la DREAL. | — |
| `S_SIG_HA` | Surface SIG (hectares) | Réel (double) | Surface calculée sous SIG, en hectares. | — |
| `D_DESIG_AM` | Date de désignation (arrêté ministériel) | Texte (date) | Date de désignation de la ZPS par arrêté ministériel. | Format jj/mm/aaaa |
| `D_NOTIF_CE` | Date de notification à la CE | Texte (date) | Date de notification du site à la Commission européenne. | Format jj/mm/aaaa |
| `DOCOB` | État d'avancement du DOCOB | Texte | État d'avancement du document d'objectifs Natura 2000. | `0_SANS DOCOB` ; `1_DOCOB EN ELABORATION` ; `2_DOCOB ACHEVE` ; `3_DOCOB EN ANIMATION` |
| `OPERATEUR` | Opérateur | Texte | Structure opératrice chargée de la rédaction du DOCOB. | — |
| `ANIMATEUR` | Animateur | Texte | Structure animatrice chargée de la mise en œuvre du DOCOB. | — |
| `COMMENT` | Commentaire | Texte | Remarques sur le site (historique de désignation, gestion…). | — |
| `LIEN_INV` | Liens avec inventaires | Texte | Liens avec les anciens inventaires (ZICO…). | — |
| `SOURCE` | Source des données | Texte | DREAL productrice de la donnée. | `DREAL_PACA`, `DREAL_LRMP`… |
| `ECHEL_NUM` | Échelle de numérisation | Texte | Échelle de numérisation du périmètre. | `1/25 000`, `1/50 000`… |
| `D_NUM_MAJ` | Date de dernière mise à jour de la numérisation | Texte (date) | Date de la dernière mise à jour géométrique. | — |
| `D_ATT_MAJ` | Date de dernière mise à jour des attributs | Texte (date) | Date de la dernière mise à jour des données descriptives. | — |
| `COUCHE` | Nom de la couche | Texte | Nom de la couche d'origine. | `ZPS` |
| `URL_FICHE` | URL de la fiche INPN | Texte (URL) | Lien vers la fiche du site sur l'INPN. | — |
| `URL_DOCOB` | URL du DOCOB | Texte (URL) | Lien vers le document d'objectifs sur le SIDE PACA. | — |
| `URL_TEXTE` | URL du texte de désignation | Texte (URL) | Lien vers l'acte de désignation (pdf). | — |

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | DREAL Provence-Alpes-Côte d'Azur |
| Source (téléchargement) | <https://www.data.gouv.fr/datasets/sites-natura-2000-au-titre-de-la-directive-oiseaux-en-provence-alpes-cote-dazur> |
| Licence | Licence Ouverte / Open Licence version 2.0 |
| Dernière mise à jour de la source | 15 octobre 2025 |
| Label | INSPIRE |

---

## 3. DPA_P — Directive paysagère des Alpilles

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `DPA_P` |
| Titre du jeu de données source | Directive paysagère des Alpilles en Provence-Alpes-Côte d'Azur |
| Type de donnée | Couche vectorielle (périmètre de protection au titre des paysages) |
| Emprise | Massif des Alpilles (Provence-Alpes-Côte d'Azur) |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Cette directive a pour objet d'offrir, dans ce grand paysage, à chacun des partenaires des références pratiques permettant d'ajuster leurs projets pour façonner plus harmonieusement leurs multiples actions et de garantir, tout en accompagnant l'évolution, une meilleure protection des paysages des Alpilles.

Les directives de protection des paysages peuvent concerner des « paysages remarquables dont l'intérêt est établi soit par leur unité et leur cohérence, soit par leur richesse particulière en matière de patrimoine ou comme témoins de modes de vie et d'habitats ou d'activités industrielles, artisanales, agricoles et forestières ».

### Structure de la table attributaire

Champs de la table attributaire de la couche `DPA_P` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `COD_DREAL` | Code interne DREAL | Texte | Code interne de la DREAL identifiant le périmètre de la directive paysagère. | `DP01` (Alpilles) |
| `NOM` | Nom du périmètre | Texte | Nom de la directive paysagère. | Directive paysagère des Alpilles |
| `PROCED` | Procédure de protection | Texte | Type de procédure au titre de la protection des paysages. | `D` : directive de protection des paysages (art. L. 241-1 du code de l'urbanisme) |
| `D_PROCED` | Date de la procédure | Texte (date) | Date de prise de l'acte instituant la directive. | AAAA-MM-JJ (04/01/2007) |
| `S_SIG_HA` | Surface SIG (hectares) | Réel (double) | Surface calculée sous SIG, en hectares. | — |
| `SOURCE` | Source des données | Texte | Origine de la donnée (producteur, bureau d'études). | — |
| `ECHEL_NUM` | Échelle de numérisation | Texte | Échelle de numérisation du périmètre. | `1/100 000` |
| `D_NUM_MAJ` | Date de dernière mise à jour de la numérisation | Texte (date) | Date de la dernière mise à jour géométrique. | — |
| `D_ATT_MAJ` | Date de dernière mise à jour des attributs | Texte (date) | Date de la dernière mise à jour des données descriptives. | — |
| `D_CART_PDF` | Date de la cartographie PDF | Texte (date) | Date de réalisation de la cartographie réglementaire de référence. | — |
| `WEB_DREAL` | Lien web DREAL | Texte (URL) | Page de la DREAL présentant la directive paysagère. | — |

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | DREAL Provence-Alpes-Côte d'Azur |
| Source (téléchargement) | <https://www.data.gouv.fr/datasets/directive-paysagere-des-alpilles-en-provence-alpes-cote-dazur-1> |
| Licence | Licence Ouverte / Open Licence version 2.0 |
| Dernière mise à jour de la source | 15 octobre 2025 |
| Label | INSPIRE |

---

## 4. L_SITE_INSCRIT_S_R93 — Sites inscrits

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `L_SITE_INSCRIT_S_R93` |
| Titre du jeu de données source | Sites inscrits en Provence-Alpes-Côte d'Azur |
| Type de donnée | Couche vectorielle (périmètres de protection des sites et paysages) |
| Emprise | Région Provence-Alpes-Côte d'Azur |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

La législation a pour but d'assurer la préservation des monuments naturels et des sites dont le caractère artistique, historique, scientifique, légendaire ou pittoresque relève de l'intérêt général.

Issue de la loi du 2 mai 1930, la protection des sites est à présent organisée par le livre III, titre IV, chapitre 1er du code de l'environnement. De la compétence du ministère de l'écologie, cette mesure est mise en œuvre localement par la DREAL et les Unités Départementales de l'Architecture et du Patrimoine (UDAP) sous l'autorité des préfets de département.

Il existe deux niveaux de protection : le classement et l'inscription.

- **Le classement** est généralement réservé aux sites les plus remarquables à dominante naturelle dont le caractère, notamment paysager, doit être rigoureusement préservé. Les travaux y sont soumis selon leur importance à autorisation préalable du préfet ou du ministre de l'écologie. Dans ce dernier cas, l'avis de la commission départementale des sites (CDNPS) est obligatoire. Les sites sont classés après enquête publique par arrêté ministériel ou par décret en Conseil d'État.
- **L'inscription** est proposée pour des sites moins sensibles ou plus humanisés qui, sans qu'il soit nécessaire de recourir au classement, présentent suffisamment d'intérêt pour être surveillés de très près. Les travaux y sont soumis à déclaration auprès de l'Architecte des Bâtiments de France (UDAP). Celui-ci dispose d'un simple avis consultatif sauf pour les permis de démolir où son avis est conforme. Les sites sont inscrits par arrêté ministériel après avis des communes concernées et enquête publique.

La France compte aujourd'hui environ 2680 sites classés et 4794 sites inscrits, dont 217 sites classés et 358 sites inscrits en Provence-Alpes-Côte d'Azur. Ils sont de tailles et de natures extrêmement diverses.

### Structure de la table attributaire

Champs de la table attributaire de la couche `L_SITE_INSCRIT_S_R93` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `cod_diren` | Code du site (DIREN/DREAL) | Texte | Code du site attribué par la DIREN/DREAL : 93 + I (inscrit) + numéro du site. | Ex. `93I00002` |
| `nom` | Nom du site | Texte | Nom du site inscrit. | — |
| `proced` | Procédure de protection | Texte | Type d'acte instituant la protection au titre de la loi de 1930. | `A` : acte pris par arrêté ministériel (inscription) ; `D` : acte pris par décret en Conseil d'État (classement) |
| `d_proced` | Date de la procédure | Texte (date) | Date de l'acte d'inscription. | jj/mm/aaaa |
| `comment` | Commentaire | Texte | Remarques sur le site et sa numérisation. | — |
| `s_offi_ha` | Surface officielle (hectares) | Texte (réel) | Surface officielle du site mentionnée dans l'acte d'inscription, en hectares. | — |
| `s_sig_ha` | Surface SIG (hectares) | Réel (double) | Surface calculée sous SIG, en hectares. | — |
| `cod_f` | Code du site (ancienne codification) | Texte | Code du site dans l'ancienne codification. | Ex. `B 55` |
| `nom_f` | Nom du site (ancienne codification) | Texte | Nom du site dans l'ancienne codification / fiche d'origine. | — |
| `cod_offi` | Code officiel | Texte | Code officiel du site. | — |
| `source` | Source des données | Texte | Origine de la donnée. | `DREAL PACA`, `SIGMAP`… |
| `ref_num` | Référentiel de numérisation | Texte | Référentiel cartographique utilisé pour la numérisation. | Ex. `IGN Bd Parcellaire`, `IGN Bd Ortho`, `IGN Scan 25` |
| `echel_num` | Échelle de numérisation | Texte | Échelle de numérisation du périmètre. | `1/10 000`, `1/25 000` |
| `d_num_maj` | Date de dernière mise à jour de la numérisation | Texte (date) | Date de la dernière mise à jour géométrique. | — |
| `d_att_maj` | Date de dernière mise à jour des attributs | Texte (date) | Date de la dernière mise à jour des données descriptives. | — |
| `d_cart_pdf` | Date de la cartographie PDF | Texte (date) | Date de réalisation de la cartographie réglementaire de référence. | — |
| `f_info` | Fiche d'information | Texte | Existence d'une fiche descriptive du site. | `O` : oui ; `N` : non |
| `f_multi` | Multiplicité du site | Texte | Nombre d'entités géographiques composant le site. | 1, 2, 3… |
| `f_offi` | Périmètre officiel | Texte | Numérisation conforme au périmètre officiel de l'acte. | `O` : oui ; `N` : non |
| `f_cart` | Cartographie disponible | Texte | Existence de la cartographie de référence du site. | `O` : oui ; `N` : non |
| `couche` | Nom de la couche | Texte | Nom de la couche d'origine. | `SI` (sites inscrits) |
| `url_texte` | URL du texte d'inscription | Texte (URL) | Lien vers l'acte d'inscription (pdf). | — |
| `url_fiche` | URL de la fiche du site | Texte (URL) | Lien vers la fiche du site (pdf). | — |
| `gid` | Identifiant interne | Entier | Identifiant interne de l'enregistrement dans la base DREAL. | — |

### Sources et producteur

| Élément | Valeur |
|---|---|
| Diffuseur | DREAL Provence-Alpes-Côte d'Azur |
| Attributions | DREAL Provence-Alpes-Côte d'Azur (contact, détenteur des droits) |
| Source (téléchargement) | <https://www.data.gouv.fr/datasets/sites-inscrits-en-provence-alpes-cote-dazur-2> |
| Licence | Licence Ouverte / Open Licence version 2.0 |
| Dernière mise à jour de la source | 24 janvier 2026 |
| Label | INSPIRE |

---

## 5. N_ENP_APB_S_R93 — Arrêtés préfectoraux de protection de biotope (APPB)

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `N_ENP_APB_S_R93` |
| Titre du jeu de données source | Arrêté Préfectoral de Protection de Biotope (APPB) en Provence-Alpes-Côte d'Azur |
| Type de donnée | Couche vectorielle (périmètres de protection réglementaire) |
| Emprise | Région Provence-Alpes-Côte d'Azur |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Les arrêtés de protection de biotope concernent les milieux naturels peu exploités par l'homme et abritant des espèces faunistiques non domestiques et/ou floristiques non cultivées protégées au titre des articles L. 411-1 et L. 411-2 du Code de l'environnement.

L'objectif est de prévenir la disparition des espèces protégées grâce à des mesures de conservation de leurs biotopes : nécessaires à leur alimentation, à leur reproduction, à leur repos ou à leur survie, ces biotopes peuvent être constitués par des mares, des marécages, des marais, des haies, des bosquets, des landes, des dunes, des pelouses ou par toutes autres formations naturelles peu exploitées par l'homme.

### Structure de la table attributaire

Champs de la table attributaire de la couche `N_ENP_APB_S_R93` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `id_local` | Identifiant local | Texte | Identifiant du site géré localement par la DREAL. | — |
| `id_mnhn` | Identifiant MNHN / INPN | Texte | Identifiant national de l'espace protégé attribué par le MNHN (format FR380xxxx pour les APPB). | — |
| `nom_site` | Nom du site | Texte | Nom de l'arrêté de protection de biotope. | — |
| `date_crea` | Date de création / de l'arrêté | Texte (date) | Date de prise de l'arrêté préfectoral. | AAAA/MM/JJ |
| `modif_adm` | Date de modification administrative | Date | Date de la dernière modification administrative (nouvel arrêté, abrogation…). | — |
| `modif_geo` | Date de modification géométrique | Date | Date de la dernière modification de la géométrie. | — |
| `url_fiche` | URL de la fiche INPN | Texte (URL) | Lien vers la fiche de l'espace protégé sur l'INPN. | — |
| `surf_off` | Surface officielle (hectares) | Réel (double) | Surface officielle mentionnée dans l'arrêté, en hectares. | — |
| `acte_deb` | Acte instituant (référence et date) | Texte | Référence et date de l'acte instituant la protection. | — |
| `acte_fin` | Acte abrogeant (référence et date) | Texte | Référence et date de l'acte mettant fin à la protection, le cas échéant. | — |
| `gest_site` | Gestionnaire du site | Texte | Structure gestionnaire ou assurant le suivi du site. | — |
| `operateur` | Opérateur / service en charge | Texte | Service de l'État en charge de la donnée (DREAL, DDT(M)…). | — |
| `precision` | Précision de la numérisation | Texte | Niveau de précision du tracé numérique. | `NE` ; `M`… |
| `src_geom` | Source géométrique | Texte | Échelle ou référentiel de la géométrie d'origine. | `1/5 000`, `1/25 000`, `1/50 000`… |
| `src_annee` | Année de la source géométrique | Texte | Année du référentiel utilisé pour la numérisation. | Ex. 2023 |
| `marin` | Site marin | Texte | Indique si le site est (partiellement) en domaine marin. | `OUI`/`NON` (ou `T`/`F`) |
| `motif_prot` | Motif de la protection | Texte | Motifs de la protection (espèces et habitats concernés). | — |
| `proced` | Procédure de protection | Texte | Type d'acte instituant la protection. | `A` : arrêté préfectoral |
| `s_sig_ha` | Surface SIG (hectares) | Réel (double) | Surface calculée sous SIG, en hectares. | — |
| `comment` | Commentaire | Texte | Remarques sur le site (espèces protégées, milieux…). | — |
| `d_att_maj` | Date de dernière mise à jour des attributs | Texte (date) | Date de la dernière mise à jour des données descriptives. | — |
| `d_cart_pdf` | Date de la cartographie PDF | Texte (date) | Date de réalisation de la cartographie réglementaire de référence. | — |
| `couche` | Nom de la couche | Texte | Nom de la couche d'origine. | `APB` |
| `url_texte` | URL de l'arrêté | Texte (URL) | Lien vers l'arrêté préfectoral (pdf). | — |
| `gid` | Identifiant interne | Entier | Identifiant interne de l'enregistrement dans la base DREAL. | — |
| `p1_nature` | Protection de la nature | Texte | Intérêt de protection : patrimoine naturel (faune, flore, habitats). | `T` : vrai (intérêt concerné) ; `F` : faux |
| `p2_culture` | Intérêt culturel | Texte | Intérêt de protection : patrimoine culturel. | `T`/`F` |
| `p3_paysage` | Intérêt paysager | Texte | Intérêt de protection : paysage. | `T`/`F` |
| `p4_geologi` | Intérêt géologique | Texte | Intérêt de protection : géologie. | `T`/`F` |
| `p5_speleo` | Intérêt spéléologique | Texte | Intérêt de protection : spéléologie. | `T`/`F` |
| `p6_archeo` | Intérêt archéologique | Texte | Intérêt de protection : archéologie. | `T`/`F` |
| `p7_paleob` | Intérêt paléobiologique | Texte | Intérêt de protection : paléontologie / paléobiologie. | `T`/`F` |
| `p8_anthrop` | Intérêt anthropique | Texte | Intérêt de protection : anthropologique. | `T`/`F` |
| `p9_science` | Intérêt scientifique | Texte | Intérêt de protection : scientifique. | `T`/`F` |
| `p10_public` | Accueil du public | Texte | Intérêt de protection : accueil et sensibilisation du public. | `T`/`F` |
| `p11_dd` | Intérêt développement durable | Texte | Intérêt de protection : développement durable. | `T`/`F` |
| `p12_autre` | Autre intérêt | Texte | Autre intérêt de protection. | `T`/`F` |

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | DREAL Provence-Alpes-Côte d'Azur |
| Source (téléchargement) | <https://www.data.gouv.fr/datasets/arrete-prefectoral-de-protection-de-biotope-appb-en-provence-alpes-cote-dazur> |
| Licence | Licence Ouverte / Open Licence version 2.0 |
| Dernière mise à jour de la source | 30 octobre 2026 |
| Label | INSPIRE |

---

## 6. RNN — Réserves naturelles nationales

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `RNN` |
| Titre du jeu de données source | Réserves naturelles nationales en Provence-Alpes-Côte d'Azur |
| Type de donnée | Couche vectorielle (périmètres de protection réglementaire) |
| Emprise | Région Provence-Alpes-Côte d'Azur |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Une réserve naturelle nationale et son périmètre de protection associé font partie des espaces naturels protégés (ENP) qui sont des zones désignées ou gérées dans un cadre international, communautaire, national ou local en vue d'atteindre des objectifs spécifiques de conservation du patrimoine naturel.

Une réserve naturelle nationale est un espace protégé terrestre ou marin, créé par l'État, et dont le patrimoine naturel est exceptionnel, tant sur le plan de la biodiversité que parfois sur celui de la géodiversité. Un classement en réserve naturelle nationale intervient pour assurer la conservation de ce patrimoine exceptionnel. Il s'agit d'un espace fortement réglementé, soustrait à toute intervention artificielle susceptible de le dégrader et qui bénéficie d'un plan de gestion. Elle se classe en catégories Ia, III ou V de l'UICN (selon la réglementation et les objectifs de gestion mis en place).

Plusieurs réserves naturelles nationales bénéficient d'une superficie additionnelle en « zone tampon » protégée par ce dispositif. Selon les cas on distingue les périmètres de protection sensu stricto pris par arrêté préfectoral, et les zones de protection définies par décret. Les périmètres de protection peuvent être vastes et définis à partir d'une liste de communes notamment dans le cas des réserves géologiques.

**Références légales** : articles L332-1 à L332-27, R332-1 à R332-29, R332-47 à R332-48 et R332-66 à R332-81 du code de l'environnement.

### Structure de la table attributaire

Champs de la table attributaire de la couche `RNN` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `id_local` | Identifiant local | Texte | Identifiant du site : `RNN` + numéro national, ou `PPGxxx` pour les périmètres de protection de réserves géologiques. | Ex. `RNN73`, `PPG001` |
| `prn_asso` | Périmètre de protection associé | Texte | Identifiant du périmètre de protection associé à la réserve. | — |
| `code_r_enp` | Code du type d'espace protégé | Texte | Code du type d'espace protégé. | `RNN` : réserve naturelle nationale ; `PRNN` : périmètre de protection de RNN |
| `nom_site` | Nom du site | Texte | Nom de la réserve naturelle (ou du périmètre de protection). | — |
| `date_crea` | Date de création | Date | Date de création de la réserve (décret). | — |
| `modif_adm` | Date de modification administrative | Date | Date de la dernière modification administrative (décret modificatif…). | — |
| `modif_geo` | Date de modification géométrique | Date | Date de la dernière modification de la géométrie. | — |
| `url_fiche` | URL de la fiche INPN | Texte (URL) | Lien vers la fiche de la réserve sur l'INPN. | — |
| `surf_off` | Surface officielle (hectares) | Réel (double) | Surface officielle mentionnée dans le décret de création, en hectares. | — |
| `acte_deb` | Acte instituant (référence et date) | Texte | Référence de l'espace protégé + date de l'acte instituant (décret de création). | Ex. `FR360007319841106` |
| `acte_fin` | Acte abrogeant (référence et date) | Texte | Référence + date de l'acte mettant fin à la protection, le cas échéant. | — |
| `gest_site` | Gestionnaire du site | Texte | Structure gestionnaire de la réserve. | — |
| `operateur` | Opérateur / service en charge | Texte | Service de l'État en charge de la donnée. | `DREAL PROVENCE-ALPES-COTE-D'AZUR` |
| `src_geom` | Source géométrique | Texte | Référentiel utilisé pour la numérisation. | Ex. `BD Carto`, `BDP` (BD Parcellaire) |
| `src_annee` | Année de la source géométrique | Texte | Année du référentiel utilisé. | — |
| `marin` | Site marin | Texte | Indique si le site est (partiellement) en domaine marin. | `T` : oui ; `F` : non |
| `id_mnhn` | Identifiant MNHN / INPN | Texte | Identifiant national de l'espace protégé (format FR360xxxx, FR950xxxx pour les périmètres de protection). | — |
| `precision` | Précision de la numérisation | Texte | Niveau de précision du tracé numérique. | `M`… |
| `surf_sig` | Surface SIG (hectares) | Réel (double) | Surface calculée sous SIG, en hectares. | — |
| `gid` | Identifiant interne | Entier | Identifiant interne de l'enregistrement dans la base DREAL. | — |
| `p1_nature` | Protection de la nature | Texte | Intérêt de protection : patrimoine naturel (faune, flore, habitats). | `T` : vrai (intérêt concerné) ; `F` : faux |
| `p2_culture` | Intérêt culturel | Texte | Intérêt de protection : patrimoine culturel. | `T`/`F` |
| `p3_paysage` | Intérêt paysager | Texte | Intérêt de protection : paysage. | `T`/`F` |
| `p4_geologi` | Intérêt géologique | Texte | Intérêt de protection : géologie. | `T`/`F` |
| `p5_speleo` | Intérêt spéléologique | Texte | Intérêt de protection : spéléologie. | `T`/`F` |
| `p6_archeo` | Intérêt archéologique | Texte | Intérêt de protection : archéologie. | `T`/`F` |
| `p7_paleob` | Intérêt paléobiologique | Texte | Intérêt de protection : paléontologie / paléobiologie. | `T`/`F` |
| `p8_anthrop` | Intérêt anthropique | Texte | Intérêt de protection : anthropologique. | `T`/`F` |
| `p9_science` | Intérêt scientifique | Texte | Intérêt de protection : scientifique. | `T`/`F` |
| `p10_public` | Accueil du public | Texte | Intérêt de protection : accueil et sensibilisation du public. | `T`/`F` |
| `p11_dd` | Intérêt développement durable | Texte | Intérêt de protection : développement durable. | `T`/`F` |
| `p12_autre` | Autre intérêt | Texte | Autre intérêt de protection. | `T`/`F` |

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | DREAL Provence-Alpes-Côte d'Azur |
| Source (téléchargement) | <https://www.data.gouv.fr/datasets/reserves-naturelles-nationales-en-provence-alpes-cote-dazur> |
| Licence | Licence Ouverte / Open Licence version 2.0 |
| Dernière mise à jour de la source | 7 août 2026 |
| Label | INSPIRE |

---

## 7. RNR — Réserves naturelles régionales

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `RNR` |
| Titre du jeu de données source | Réserves naturelles régionales (extrait régional de la couche nationale des espaces protégés de l'INPN) |
| Type de donnée | Couche vectorielle (périmètres de protection réglementaire) |
| Emprise | Région Provence-Alpes-Côte d'Azur (données issues de la couche nationale, filtrée sur la région) |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Selon l'Union Internationale pour la Conservation de la Nature (UICN), un espace protégé est « un espace géographique clairement défini, reconnu, consacré et géré, par tout moyen efficace, juridique ou autre, afin d'assurer à long terme la conservation de la nature ainsi que les services écosystémiques et les valeurs culturelles qui lui sont associés ».

La désignation des espaces naturels protégés est une composante majeure des stratégies de protection et de gestion du patrimoine naturel. À ce titre, il existe en France différents outils de protection dont la diversité reflète la multiplicité des acteurs, des objectifs et des types de gestion.

Les réserves naturelles régionales (RNR) sont des espaces naturels protégés créés par les régions, en application des articles L. 332-1 et suivants du code de l'environnement. La couche provient du programme « Espaces protégés » de l'INPN, qui rassemble et harmonise les données fournies par les gestionnaires et les structures régionales de l'État.

### Structure de la table attributaire

Champs de la table attributaire de la couche `RNR` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `id_mnhn` | Identifiant MNHN / INPN | Texte | Identifiant national de l'espace protégé attribué par le MNHN (équiv. `CdENP` dans le standard CNIG). | — |
| `nom` | Nom de l'espace | Texte | Nom de l'espace protégé (équiv. `NomENP`). | — |
| `date_crea_sign` | Date de création / de signature de l'acte | Texte (date) | Date de création ou de signature de l'acte instituant la protection (équiv. `DateCreaENP`). | — |
| `date_modif_geo` | Date de mise à jour technique | Texte (date) | Date de dernière mise à jour de la géométrie (équiv. `DateMajTechENP`). | — |
| `lien_fiche` | Lien fiche INPN | Texte (URL) | Lien vers la fiche de l'espace sur l'INPN (équiv. `LienFicheENP` ; souvent vide dans le format COVADIS). | — |
| `type_espace` | Type d'espace protégé | Texte | Type d'espace protégé (équiv. `TypeENP`). | Voir la liste des 33 types nationaux ; modalités principales ci-dessous |
| `objectif_protection` | Objectif de protection | Texte | Objectif principal de protection de l'espace (équiv. `ObjectifProtectionENP`). | `Nature` ; `Géologie` |
| `statut` | Statut de l'espace | Texte | Statut de l'espace protégé (équiv. `StatutENP` ; champ non renseigné dans la livraison COVADIS). | — |
| `superficie_ha` | Surface officielle (hectares) | Réel (double) | Surface officielle de l'espace, en hectares (équiv. `SurfOffENP`). | — |
| `cd_type_milieu` | Type de milieu | Texte | Indique si l'espace est terrestre, marin ou mixte (équiv. `ENPMarin`). | `TER` : terrestre ; `MER` : marin ; `MIX` : mixte |
| `ref_carto_nom` | Référentiel cartographique | Texte | Nom du jeu de données de référence utilisé pour la géométrie (équiv. `JDDGeoRefENP`). | Ex. `BD Parcellaire`, `BD ORTHO`… |
| `ref_carto_version` | Version du référentiel | Texte | Millésime/version du référentiel utilisé (équiv. `VersionRefENP`). | Ex. 2025 |
| `doc_gestion` | Document de gestion | Texte (booléen) | Existence d'un document de gestion sur l'espace (équiv. `PresDocGestENP`). | `true`/`false` |

Modalités de `type_espace` pour cette couche : `Réserve naturelle régionale` (et `Périmètre de protection d'une réserve naturelle régionale ou de Corse` pour les périmètres associés). La couche est un extrait régional de la table nationale `sig_metrop` (livraison COVADIS du programme « Espaces protégés » de l'INPN), filtrée sur ce type d'espace.

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | Muséum National d'Histoire Naturelle (MNHN) — PatriNat, centre d'expertise et de données sur le patrimoine naturel (INPN) |
| Source (téléchargement) | <https://assets.patrinat.fr/files/donnees/ep/EP.zip> |
| Fiche de métadonnées du programme | <https://www.data.gouv.fr/datasets/inpn-donnees-du-programme-espaces-proteges> |
| Licence | Licence ouverte (à vérifier sur la fiche source du programme INPN « Espaces protégés ») |
| Dernière mise à jour de la fiche source | 8 octobre 2026 |
| Format source | Shapefile / GeoPackage (standard COVADIS « Espaces protégés ») |

---

## 8. znieff1 — ZNIEFF de type I

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `znieff1` |
| Titre du jeu de données source | Inventaire des Zones Naturelles d'Intérêt Écologique, Faunistique et Floristique — ZNIEFF de type I (extrait régional de la couche nationale de l'INPN) |
| Type de donnée | Couche vectorielle (périmètres d'inventaire) |
| Emprise | Région Provence-Alpes-Côte d'Azur (données issues de la couche nationale, filtrée sur la région) |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Lancé en 1982, l'inventaire des Zones Naturelles d'Intérêt Écologique Faunistique et Floristique (ZNIEFF) a pour objectif d'identifier et de décrire des secteurs présentant de fortes capacités biologiques et un bon état de conservation. On distingue 2 types de ZNIEFF :

- **les ZNIEFF de type I** : secteurs de grand intérêt biologique ou écologique ;
- les ZNIEFF de type II : grands ensembles naturels riches et peu modifiés, offrant des potentialités biologiques importantes.

L'inventaire ZNIEFF concerne progressivement l'ensemble du territoire français (Métropole, près de 15 000 zones : 12 915 de type I et 1 921 de type II ; Outre-Mer, milieu terrestre et marin).

Une modernisation nationale (mise à jour et harmonisation de la méthode de réalisation de cet inventaire) a été lancée en 1996 afin d'améliorer l'état des connaissances, d'homogénéiser les critères d'identification des ZNIEFF et de faciliter la diffusion de leur contenu. En 2004, près de 2000 ZNIEFF avaient été modernisées et validées au plan national sur 3 régions (Limousin, Normandie, Champagne-Ardenne).

Cet inventaire est devenu aujourd'hui un des éléments majeurs de la politique de protection de la nature. Il doit être consulté dans le cadre de projets d'aménagement du territoire (documents d'urbanisme, création d'espaces protégés, élaboration de schémas départementaux de carrières, etc.). **La ZNIEFF est un outil d'inventaire, non de protection réglementaire.**

### Structure de la table attributaire

Champs de la table attributaire de la couche `znieff1` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `OBJECTID` | Identifiant interne | Entier | Identifiant interne de l'entité. | — |
| `ID_MNHN` | Identifiant national (NM_SFFZN) | Texte | Identifiant national de la ZNIEFF attribué par le MNHN. | Ex. 00000725 |
| `NOM` | Nom de la ZNIEFF | Texte | Nom de la zone naturelle d'intérêt écologique, faunistique et floristique. | — |
| `ID_ORG` | Identifiant organisme | Texte | Identifiant de la ZNIEFF utilisé par l'organisme régional (CRB / SINP régional). | — |
| `CD_SIG` | Code SIG | Texte | Code du périmètre dans le SIG régional (code de l'organisme). | — |
| `PRECIS_X` | Précision en X | Entier | Précision de localisation du centroïde sur l'axe X (mètres). | — |
| `PRECIS_Y` | Précision en Y | Entier | Précision de localisation du centroïde sur l'axe Y (mètres). | — |
| `X_PROJ` | Coordonnée X projetée | Entier | Coordonnée X du centroïde dans la projection. | — |
| `Y_PROJ` | Coordonnée Y projetée | Entier | Coordonnée Y du centroïde dans la projection. | — |
| `GENERATION` | Génération de l'inventaire | Texte | Génération de l'inventaire ZNIEFF. | `G2` : 2ᵉ génération (ZNIEFF modernisées) ; `G1` : 1ʳᵉ génération |
| `SUPERFICIE` | Surface (hectares) | Réel (double) | Surface de la ZNIEFF, en hectares. | — |
| `SE_ANNO_CA` | Champ technique (annotation) | Texte | Champ technique issu de la conversion ArcGIS (annotation), sans valeur métier. | — |

La livraison nationale ZNIEFF (standard « données de production ») comprend également la table attributaire complémentaire `REF_ZNIEFF.csv` (altitudes min/max, surface, rédacteurs, commentaires…) joignable à la couche SIG par l'identifiant `ID_MNHN` (`NM_SFFZN`). `TY_ZONE` = `1` pour les ZNIEFF de type I.

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | Muséum National d'Histoire Naturelle (MNHN) — PatriNat (INPN) |
| Source (téléchargement) | <https://assets.patrinat.fr/files/donnees/znieff/ZNIEFF.zip> |
| Fiche de métadonnées du programme | <https://www.data.gouv.fr/datasets/inpn-donnees-du-programme-znieff> |
| Licence | Licence Ouverte / Open Licence |
| Dernière mise à jour de la fiche source | 8 octobre 2026 |
| Format source | Shapefile / GeoPackage (standard COVADIS ZNIEFF) |

---

## 9. znieff2 — ZNIEFF de type II

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `znieff2` |
| Titre du jeu de données source | Inventaire des Zones Naturelles d'Intérêt Écologique, Faunistique et Floristique — ZNIEFF de type II (extrait régional de la couche nationale de l'INPN) |
| Type de donnée | Couche vectorielle (périmètres d'inventaire) |
| Emprise | Région Provence-Alpes-Côte d'Azur (données issues de la couche nationale, filtrée sur la région) |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Lancé en 1982, l'inventaire des Zones Naturelles d'Intérêt Écologique Faunistique et Floristique (ZNIEFF) a pour objectif d'identifier et de décrire des secteurs présentant de fortes capacités biologiques et un bon état de conservation. On distingue 2 types de ZNIEFF :

- les ZNIEFF de type I : secteurs de grand intérêt biologique ou écologique ;
- **les ZNIEFF de type II** : grands ensembles naturels riches et peu modifiés, offrant des potentialités biologiques importantes.

L'inventaire ZNIEFF concerne progressivement l'ensemble du territoire français (Métropole, près de 15 000 zones : 12 915 de type I et 1 921 de type II ; Outre-Mer, milieu terrestre et marin).

Une modernisation nationale (mise à jour et harmonisation de la méthode de réalisation de cet inventaire) a été lancée en 1996 afin d'améliorer l'état des connaissances, d'homogénéiser les critères d'identification des ZNIEFF et de faciliter la diffusion de leur contenu. En 2004, près de 2000 ZNIEFF avaient été modernisées et validées au plan national sur 3 régions (Limousin, Normandie, Champagne-Ardenne).

Cet inventaire est devenu aujourd'hui un des éléments majeurs de la politique de protection de la nature. Il doit être consulté dans le cadre de projets d'aménagement du territoire (documents d'urbanisme, création d'espaces protégés, élaboration de schémas départementaux de carrières, etc.). **La ZNIEFF est un outil d'inventaire, non de protection réglementaire.**

### Structure de la table attributaire

Champs de la table attributaire de la couche `znieff2` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `OBJECTID` | Identifiant interne | Entier | Identifiant interne de l'entité. | — |
| `ID_MNHN` | Identifiant national (NM_SFFZN) | Texte | Identifiant national de la ZNIEFF attribué par le MNHN. | Ex. 00000725 |
| `NOM` | Nom de la ZNIEFF | Texte | Nom de la zone naturelle d'intérêt écologique, faunistique et floristique. | — |
| `ID_ORG` | Identifiant organisme | Texte | Identifiant de la ZNIEFF utilisé par l'organisme régional (CRB / SINP régional). | — |
| `CD_SIG` | Code SIG | Texte | Code du périmètre dans le SIG régional (code de l'organisme). | — |
| `PRECIS_X` | Précision en X | Entier | Précision de localisation du centroïde sur l'axe X (mètres). | — |
| `PRECIS_Y` | Précision en Y | Entier | Précision de localisation du centroïde sur l'axe Y (mètres). | — |
| `X_PROJ` | Coordonnée X projetée | Entier | Coordonnée X du centroïde dans la projection. | — |
| `Y_PROJ` | Coordonnée Y projetée | Entier | Coordonnée Y du centroïde dans la projection. | — |
| `GENERATION` | Génération de l'inventaire | Texte | Génération de l'inventaire ZNIEFF. | `G2` : 2ᵉ génération (ZNIEFF modernisées) ; `G1` : 1ʳᵉ génération |
| `SUPERFICIE` | Surface (hectares) | Réel (double) | Surface de la ZNIEFF, en hectares. | — |
| `SE_ANNO_CA` | Champ technique (annotation) | Texte | Champ technique issu de la conversion ArcGIS (annotation), sans valeur métier. | — |

Table attributaire identique à la couche ZNIEFF de type I. Dans `REF_ZNIEFF.csv`, `TY_ZONE` = `2` pour les ZNIEFF de type II ; le champ `NM_SFFZN_PARENT` permet de lier une ZNIEFF de type I à l'ensemble de type II qui l'inclut.

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | Muséum National d'Histoire Naturelle (MNHN) — PatriNat (INPN) |
| Source (téléchargement) | <https://assets.patrinat.fr/files/donnees/znieff/ZNIEFF.zip> |
| Fiche de métadonnées du programme | <https://www.data.gouv.fr/datasets/inpn-donnees-du-programme-znieff> |
| Licence | Licence Ouverte / Open Licence |
| Dernière mise à jour de la fiche source | 8 octobre 2026 |
| Format source | Shapefile / GeoPackage (standard COVADIS ZNIEFF) |

---

## 10. cdl — Conservatoire du littoral

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `cdl` |
| Titre du jeu de données source | Terrains acquis ou affectés au Conservatoire du littoral (extrait régional de la couche nationale des espaces protégés de l'INPN) |
| Type de donnée | Couche vectorielle (périmètres de terrains acquis en maîtrise foncière) |
| Emprise | Région Provence-Alpes-Côte d'Azur (données issues de la couche nationale, filtrée sur la région) |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Selon l'Union Internationale pour la Conservation de la Nature (UICN), un espace protégé est « un espace géographique clairement défini, reconnu, consacré et géré, par tout moyen efficace, juridique ou autre, afin d'assurer à long terme la conservation de la nature ainsi que les services écosystémiques et les valeurs culturelles qui lui sont associés ».

La couche localise les parcelles et terrains acquis ou affectés au **Conservatoire du littoral** dans un but de protection des sites naturels, en France métropolitaine et outre-mer. Établissement public créé par la loi du 10 juillet 1975, le Conservatoire du littoral mène une politique de maîtrise foncière du littoral, de sauvegarde des sites naturels et de leur ouverture au public. La donnée provient du programme « Espaces protégés » de l'INPN, qui rassemble et harmonise les données fournies par le Conservatoire du littoral ; les données sont fournies selon le standard COVADIS « Espaces protégés ».

**Statut** : maîtrise foncière (protection par acquisition), et non protection réglementaire du périmètre en tant que telle.

### Structure de la table attributaire

Champs de la table attributaire de la couche `cdl` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `id_mnhn` | Identifiant MNHN / INPN | Texte | Identifiant national de l'espace protégé attribué par le MNHN (équiv. `CdENP` dans le standard CNIG). | — |
| `nom` | Nom de l'espace | Texte | Nom de l'espace protégé (équiv. `NomENP`). | — |
| `date_crea_sign` | Date de création / de signature de l'acte | Texte (date) | Date de création ou de signature de l'acte instituant la protection (équiv. `DateCreaENP`). | — |
| `date_modif_geo` | Date de mise à jour technique | Texte (date) | Date de dernière mise à jour de la géométrie (équiv. `DateMajTechENP`). | — |
| `lien_fiche` | Lien fiche INPN | Texte (URL) | Lien vers la fiche de l'espace sur l'INPN (équiv. `LienFicheENP` ; souvent vide dans le format COVADIS). | — |
| `type_espace` | Type d'espace protégé | Texte | Type d'espace protégé (équiv. `TypeENP`). | Voir la liste des 33 types nationaux ; modalités principales ci-dessous |
| `objectif_protection` | Objectif de protection | Texte | Objectif principal de protection de l'espace (équiv. `ObjectifProtectionENP`). | `Nature` ; `Géologie` |
| `statut` | Statut de l'espace | Texte | Statut de l'espace protégé (équiv. `StatutENP` ; champ non renseigné dans la livraison COVADIS). | — |
| `superficie_ha` | Surface officielle (hectares) | Réel (double) | Surface officielle de l'espace, en hectares (équiv. `SurfOffENP`). | — |
| `cd_type_milieu` | Type de milieu | Texte | Indique si l'espace est terrestre, marin ou mixte (équiv. `ENPMarin`). | `TER` : terrestre ; `MER` : marin ; `MIX` : mixte |
| `ref_carto_nom` | Référentiel cartographique | Texte | Nom du jeu de données de référence utilisé pour la géométrie (équiv. `JDDGeoRefENP`). | Ex. `BD Parcellaire`, `BD ORTHO`… |
| `ref_carto_version` | Version du référentiel | Texte | Millésime/version du référentiel utilisé (équiv. `VersionRefENP`). | Ex. 2025 |
| `doc_gestion` | Document de gestion | Texte (booléen) | Existence d'un document de gestion sur l'espace (équiv. `PresDocGestENP`). | `true`/`false` |

Modalités de `type_espace` pour cette couche : `Terrain acquis par le Conservatoire du Littoral`. La couche est un extrait régional de la table nationale `sig_metrop`, filtrée sur ce type d'espace.

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | Muséum National d'Histoire Naturelle (MNHN) — PatriNat (INPN), à partir des données du Conservatoire du littoral |
| Source (téléchargement) | <https://assets.patrinat.fr/files/donnees/ep/EP.zip> |
| Fiche de métadonnées du programme | <https://www.data.gouv.fr/datasets/inpn-donnees-du-programme-espaces-proteges> |
| Licence | Licence ouverte (à vérifier sur la fiche source du programme INPN « Espaces protégés ») |
| Dernière mise à jour de la fiche source | 8 octobre 2026 |
| Format source | Shapefile / GeoPackage (standard COVADIS « Espaces protégés ») |

---

## 11. cen — Conservatoires d'espaces naturels

### Identification

| Élément | Valeur |
|---|---|
| Nom de la couche (GeoPackage) | `cen` |
| Titre du jeu de données source | Sites des Conservatoires d'espaces naturels (extrait régional de la couche nationale des espaces protégés de l'INPN) |
| Type de donnée | Couche vectorielle (périmètres de sites gérés ou acquis) |
| Emprise | Région Provence-Alpes-Côte d'Azur (données issues de la couche nationale, filtrée sur la région) |
| Système de coordonnées | Lambert 93 (EPSG:2154) — à vérifier dans le GeoPackage |

### Description

Selon l'Union Internationale pour la Conservation de la Nature (UICN), un espace protégé est « un espace géographique clairement défini, reconnu, consacré et géré, par tout moyen efficace, juridique ou autre, afin d'assurer à long terme la conservation de la nature ainsi que les services écosystémiques et les valeurs culturelles qui lui sont associés ».

La couche localise les sites acquis ou gérés par les **Conservatoires d'espaces naturels** (CEN), fédérés au sein de la fédération des Conservatoires d'espaces naturels. La constitution de la couche nationale repose sur les dossiers transmis par les CEN (acquisition, location, gestion de moins de 18 ans, convention de gestion). La donnée provient du programme « Espaces protégés » de l'INPN, qui rassemble et harmonise ces données ; les données sont fournies selon le standard COVADIS « Espaces protégés ». Les attributs incluent notamment l'identifiant national (ID_MNHN), l'identifiant utilisé par la fédération (ID_ORG), le nom du site (NOM) et la surface (SUPE).

**Statut** : maîtrise foncière et/ou gestion contractuelle (convention), et non protection réglementaire du périmètre en tant que telle.

### Structure de la table attributaire

Champs de la table attributaire de la couche `cen` :

| Champ | Libellé | Type | Définition | Modalités |
|---|---|---|---|---|
| `id_mnhn` | Identifiant MNHN / INPN | Texte | Identifiant national de l'espace protégé attribué par le MNHN (équiv. `CdENP` dans le standard CNIG). | — |
| `nom` | Nom de l'espace | Texte | Nom de l'espace protégé (équiv. `NomENP`). | — |
| `date_crea_sign` | Date de création / de signature de l'acte | Texte (date) | Date de création ou de signature de l'acte instituant la protection (équiv. `DateCreaENP`). | — |
| `date_modif_geo` | Date de mise à jour technique | Texte (date) | Date de dernière mise à jour de la géométrie (équiv. `DateMajTechENP`). | — |
| `lien_fiche` | Lien fiche INPN | Texte (URL) | Lien vers la fiche de l'espace sur l'INPN (équiv. `LienFicheENP` ; souvent vide dans le format COVADIS). | — |
| `type_espace` | Type d'espace protégé | Texte | Type d'espace protégé (équiv. `TypeENP`). | Voir la liste des 33 types nationaux ; modalités principales ci-dessous |
| `objectif_protection` | Objectif de protection | Texte | Objectif principal de protection de l'espace (équiv. `ObjectifProtectionENP`). | `Nature` ; `Géologie` |
| `statut` | Statut de l'espace | Texte | Statut de l'espace protégé (équiv. `StatutENP` ; champ non renseigné dans la livraison COVADIS). | — |
| `superficie_ha` | Surface officielle (hectares) | Réel (double) | Surface officielle de l'espace, en hectares (équiv. `SurfOffENP`). | — |
| `cd_type_milieu` | Type de milieu | Texte | Indique si l'espace est terrestre, marin ou mixte (équiv. `ENPMarin`). | `TER` : terrestre ; `MER` : marin ; `MIX` : mixte |
| `ref_carto_nom` | Référentiel cartographique | Texte | Nom du jeu de données de référence utilisé pour la géométrie (équiv. `JDDGeoRefENP`). | Ex. `BD Parcellaire`, `BD ORTHO`… |
| `ref_carto_version` | Version du référentiel | Texte | Millésime/version du référentiel utilisé (équiv. `VersionRefENP`). | Ex. 2025 |
| `doc_gestion` | Document de gestion | Texte (booléen) | Existence d'un document de gestion sur l'espace (équiv. `PresDocGestENP`). | `true`/`false` |

Modalités de `type_espace` pour cette couche : `Terrain acquis (ou assimilé) par un Conservatoire d'espaces naturels` et `Terrain géré (location, convention de gestion) par un Conservatoire d'espaces naturels`. La couche est un extrait régional de la table nationale `sig_metrop`, filtrée sur ces types d'espace.

### Sources et producteur

| Élément | Valeur |
|---|---|
| Producteur | Muséum National d'Histoire Naturelle (MNHN) — PatriNat (INPN), à partir des données de la fédération des Conservatoires d'espaces naturels |
| Source (téléchargement) | <https://assets.patrinat.fr/files/donnees/ep/EP.zip> |
| Fiche de métadonnées du programme | <https://www.data.gouv.fr/datasets/inpn-donnees-du-programme-espaces-proteges> |
| Licence | Licence ouverte (à vérifier sur la fiche source du programme INPN « Espaces protégés ») |
| Dernière mise à jour de la fiche source | 8 octobre 2026 |
| Format source | Shapefile / GeoPackage (standard COVADIS « Espaces protégés ») |
