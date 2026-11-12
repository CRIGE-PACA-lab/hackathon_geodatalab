#PPRI - 13 

Deux jeux de données sont disponibles dans ce geopackage : 

1. [Couche 'n_document_pprn_s_013' : Document des Plans de Prévention des Risques Naturels (PPRN) sur le département des Bouches-du-Rhône](## Couche 'n_document_pprn_s_013' : Document des Plans de Prévention des Risques Naturels (PPRN) sur le département des Bouches-du-Rhône)
2. [Couche 'n_zonereg_pprn_s_013' : Zone réglementée du Plan de Prévention des Risques Inondation (PPRI) dans les Bouches-du-Rhône](## Couche 'n_zonereg_pprn_s_013' : Zone réglementée du Plan de Prévention des Risques Inondation (PPRI) dans les Bouches-du-Rhône)

---


## Couche 'n_document_pprn_s_013' : Document des Plans de Prévention des Risques Naturels (PPRN) sur le département des Bouches-du-Rhône


### 📌 Identité du jeu de données

| Élément | Valeur |
|---|---|
| **Titre** | Document des Plans de Prévention des Risques Naturels (PPRN) sur le département des Bouches-du-Rhône |
| **Producteur / Détenteur des droits** | DDTM 13 (Pôle SIG et Analyse Territoriale) |
| **Diffuseur** | DDTM 13, via data.gouv.fr  |
| **Page data.gouv.fr** | [data.gouv.fr/datasets/document-des-plans-de-prevention-des-risques-naturels-pprn-sur-le-departement-des-bouches-du-rhone](https://www.data.gouv.fr/datasets/document-des-plans-de-prevention-des-risques-naturels-pprn-sur-le-departement-des-bouches-du-rhone) |
| **Date de création (data.gouv)** | 24/10/2019 |
| **Dernière mise à jour (data.gouv)** | 21/10/2026 |
| **Licence** | Licence Ouverte / Open Licence 2.0 |
| **Conformité** | Label INSPIRE ; thèmes « Risques naturels » / « Zones de gestion, de restriction ou de réglementation » |
| **Contact** | ddtm@bouches-du-rhone.gouv.fr |

### 🎯 Objet du jeu de données

Les plans de prévention des risques (PPR) ont été institués par la **loi du 2 février 1995** (dite « loi Barnier ») relative au renforcement de la protection de l'environnement. Ils constituent l'instrument essentiel de l'État en matière de prévention des risques, avec pour objectif le **contrôle du développement dans les zones exposées à un risque majeur**. Les PPR sont **approuvés par le préfet** et réalisés par la DDTM des Bouches-du-Rhône.

Ces plans réglementent l'occupation du sol ou son usage par des **interdictions de construire** ou des **prescriptions** sur les bâtiments existants ou futurs (dispositions constructives, travaux de réduction de la vulnérabilité, restrictions d'usage ou de pratiques agricoles…). Les plans peuvent être **prescrits** (en cours d'élaboration), **appliqués par anticipation** ou **approuvés**.

Chaque **document de PPRN** est représenté par un **polygone** correspondant :

- à l'ensemble des **communes concernées par le périmètre de prescription**, lorsque le PPR est à l'état prescrit ;
- à l'**enveloppe des zones réglementées**, lorsque le PPR est à l'état approuvé.

> ℹ️ **Portée de la couche** : cette table est un **index géographique des documents PPRN** (une entité ≈ un plan, identifié par son code GASPAR). Ce n'est **pas** la couche des zones réglementées elles-mêmes : chaque plan dispose de sa propre série de données géographiques (zonage réglementaire, aléas, enjeux), par ex. *Zone réglementée du PPRN de la commune d'Arles — 13DDTM20000134*.

### 🔗 Système de liaison GASPAR

Chaque document de la table `N_DOCUMENT_PPRN` est lié par son **code GASPAR** au format **`ddd[PREF|DDT|DDTM|DREAL]AAAANNNN`** (AAAA = année de référence de la procédure, NNNN = numéro d'ordre de la procédure PPR dans GASPAR) :

1. à sa **procédure administrative d'élaboration (ou de révision)** gérée dans l'application **GASPAR** (base nationale de suivi des procédures de prévention des risques) ;
2. à sa **série de données géographiques numériques constituantes**, décrite par une fiche de métadonnées dédiée de type `N_PPRN_AAAANNNN` (ex. fiche n° 0001495 du catalogue, [Géosource](https://geosource.fr)).

Exemple : le PPRI d'Arles a pour code GASPAR `13DDTM20000134` → document dans cette table + couche de zonage réglementaire diffusée séparément.

### 📋 Dictionnaire des attributs (classe `DocumentPPR` du géostandard COVADIS)

> Dictionnaire conforme au **géostandard COVADIS PPRN-PPRT** (classe `DocumentPPR`, table `N_DOCUMENT_PPRN_S_DDD`). ⚠️ Le service WFS Geo-IDE de cette couche était indisponible lors de la rédaction (erreur serveur côté diffusion) ; la liste exacte des champs du jeu diffusé est donc à confirmer via `DescribeFeatureType` ou l'archive Atom une fois le service rétabli.

| Champ | Libellé | Type | Définition |
|---|---|---|---|
| `ID_GASPAR` | Identifiant GASPAR | Texte (16) | Identifiant du document PPR dans la base GASPAR, format `ddd[PREF|DDT|DDTM|DREAL]AAAANNNN` (ex. `13DDTM20000134` pour le PPRI d'Arles) — clé de liaison avec la procédure administrative et la série géographique du plan |
| `NOM` | Nom du document | Texte | Nom complet du plan (ex. *« Plan de Prévention des Risques Naturels Prévisibles Inondation sur la commune d'Arles »*) |
| `URLFIC` | URL du dossier réglementaire | Texte | Lien de téléchargement du dossier du PPR (note de présentation, plan de zonage réglementaire, règlement) |
| `DATE_PRESCRIPT` | Date de prescription | Date | Date de l'arrêté préfectoral de prescription (lancement de la procédure d'élaboration) |
| `DATE_APPRO` | Date d'approbation | Date | Date de l'arrêté préfectoral d'approbation (opposabilité ; vaut servitude d'utilité publique, art. L. 562-4 C. env.) |
| `DATE_MISE_AJOUR` | Date de mise à jour | Date | Date de dernière mise à jour du dossier (révision ou modification) |
| `DATE_DIFF_PLU` | Date de diffusion au PLU | Date | Date de transmission du dossier au maire pour annexion au document d'urbanisme |
| `ETAT` | État de la procédure | Texte | État d'avancement : **Prescrit**, **En cours d'élaboration**, **Approuvé**, **Appliqué par anticipation** |
| `RISQUE` | Typologie du risque | Texte | Code(s) du/des risque(s) couvert(s) selon la nomenclature GASPAR (ex. `100` = inondation, `21` = mouvement de terrain, `10` = avalanche…) — un PPR couvrant plusieurs risques est dit « multirisques » |
| `FAMILLE` | Famille de risque | Texte | Famille de risque au sens GASPAR |

> ℹ️ Les dates d'enquête publique, de consultation et de signature, ainsi que les autres informations de procédure, sont gérées dans **GASPAR** et ne figurent donc pas dans le noyau du géostandard : la table géographique reste volontairement minimale.

### 🎨 Sémantique des périmètres

- **PPR prescrit** → polygone = **périmètre de prescription** (ensemble des communes concernées) ;
- **PPR approuvé (ou appliqué par anticipation)** → polygone = **enveloppe des zones réglementées** du plan.

Un PPR approuvé vaut **servitude d'utilité publique** (art. L. 562-4 du Code de l'environnement) et doit être annexé au PLU (art. L. 153-16 du Code de l'urbanisme). Le non-respect de ses dispositions est punissable (art. L. 562-5 C. env.).

### 📚 Cadre réglementaire et référentiels

- **Loi n° 95-101 du 2 février 1995** (« loi Barnier ») — institution des PPR ;
- **Art. L. 562-1 à L. 562-9 du Code de l'environnement** — régime des PPR ;
- **Géostandard COVADIS PPRN-PPRT** (CNIG) — modèle de données des classes `DocumentPPR`, `ZonePPR`, `SecteurRefuge`, `AleaPPR`, `EnjeuPPR` ;
- **Base nationale GASPAR** ([georisques.gouv.fr](https://www.georisques.gouv.fr)) — application de gestion assistée des procédures administratives relatives aux risques naturels et technologiques.

### ⚖️ Limites d'usage

- Couche **d'index des documents** : ne pas confondre avec le **zonage réglementaire** d'un plan (diffusé couche par couche, cf. séries `N_PPRN_AAAANNNN`) ;
- Les limites des polygones sont **indicatives** (périmètre de prescription ou enveloppe du zonage) : la valeur juridique d'un PPR réside dans son **règlement et sa carte de zonage réglementaire** opposables ;
- Les ressources « intranet » (RIE) ne sont pas accessibles hors réseau interministériel ;
- Actualité : la géométrie reflète l'état de la base DDTM 13 à la date de la dernière publication (21/10/2026) ; la liste officielle et à jour des procédures reste **GASPAR / Géorisques**.



---

## Couche 'n_zonereg_pprn_s_013' : Zone réglementée du Plan de Prévention des Risques Inondation (PPRI) dans les Bouches-du-Rhône

Pour les PPRI, le Code de l'environnement (art. L. 562-1) définit deux catégories de zones : les **zones exposées aux risques** et les **zones non directement exposées** mais sur lesquelles des mesures peuvent être prévues pour éviter d'aggraver le risque. En fonction du niveau d'aléa, chaque zone fait l'objet d'un **règlement opposable**.

### 📌 Identité du jeu de données

| Élément | Valeur |
|---|---|
| **Titre** | Zone réglementée du Plan de Prévention des risques inondations — Bouches-du-Rhône |
| **Diffuseur / producteur** | DDTM 13 |
| **Risque couvert** | Inondation |
| **Type de ressource** | Jeu de données (vecteur, geopackage — polygones) |
| **Résolution spatiale** | 1 / 2 500 |
| **Licence** | Licence Ouverte / Open Licence version 2.0 |

### 📐 Cadre réglementaire & contenu du zonage

Les limites d'une zone réglementée sont représentées sur les **documents graphiques du PPR**. Elles sont généralement calées sur les phénomènes naturels, qui ne suivent ni le découpage cadastral ni les limites administratives. Les limites réglementaires sont déterminées en fonction de **l'emprise calculée des phénomènes dangereux**. Certains PPR peuvent contenir des règlements associés à des figurés linéaires ou ponctuels (cavités, axes de ruissellement…).

Les règlements distinguent généralement **trois types de zones** :

1. **« Zones d'interdiction de construire », dites zones rouges** — niveau d'aléa fort : la règle générale est l'interdiction de construire ;
2. **« Zones soumises à prescriptions », dites zones bleues** — niveau d'aléa moyen : les projets sont soumis à des prescriptions adaptées au type d'enjeu ;
3. **Zones non directement exposées aux risques** mais où des constructions, ouvrages, aménagements ou exploitations (agricoles, forestières, artisanales, commerciales ou industrielles) pourraient **aggraver des risques ou en provoquer de nouveaux** — soumises à interdictions ou prescriptions (art. L. 562-1 du Code de l'environnement). Cette catégorie ne s'applique qu'aux PPR naturels.

### 🗂️ Contenu de la table attributaire

La couche `n_zonereg_pprn_s_013` est un geopackage de **polygones** qui comporte **15 champs** :

> ℹ️ Descriptions issues du standard COVADIS ; la structure a été vérifiée par interrogation du service WFS (DescribeFeatureType) de la DDTM 13.

| Champ | Description | Type |
|---|---|---|
| `ID_MAP` | Identifiant interne de l'objet géographique | Entier |
| `ID_ZONE` | Identifiant unique de la zone réglementée | Texte |
| `ID_GASPAR` | Identifiant du PPR dans la base GASPAR (dossier 13DDTM20000134) | Texte |
| `NOM` | Nom du PPR (commune d'Arles) | Texte |
| `CODEZONE` | Code de la zone réglementée (ex. rouge / bleue) | Texte |
| `TYPEREG` | Type de zone réglementée (zone exposée / non directement exposée) | Texte |
| `SOUMISALEA` | Soumission à l'aléa (zone directement exposée ou non) | Texte |
| `NOMFIC` | Nom du fichier du règlement associé à la zone | Texte |
| `URLFIC` | URL du fichier du règlement | Texte |
| `SRCE_GEOM` | Source géométrique (référentiel utilisé pour la numérisation) | Texte |
| `SRCE_ANNEE` | Année de la source géométrique | Texte |
| `PRECISION` | Précision de la numérisation | Texte |
| `ID_R` | Identifiant de la ressource (catalogue Geo-IDE) | Texte |
| `INSEE_COM` | Code INSEE de la commune (13004 — Arles) | Entier |

### Nomenclature du champ `TYPEREG`

Le standard CNIG des risques (géostandard PPR, héritier du standard COVADIS PPRN/PPRT) définit une **nomenclature fermée** de 6 types standardisés précisant la nature de la zone réglementée :

| Code | Modalité | Définition | Usage |
|---|---|---|---|
| `01` | **Prescription hors zone d'aléa** | Réglementation appliquant des prescriptions à une zone **non directement exposée** à l'aléa, pour ne pas aggraver le risque sur d'autres secteurs ou créer de nouveaux risques | PPRN — zones « blanches » (`nom` = « - », `codezone` = « - », `soumisalea` = « non ») |
| `02` | **Prescriptions** | Zone exposée où les projets sont admis **sous prescriptions** adaptées au type d'enjeu et d'aléa | PPRN — zones bleues |
| `03` | **Interdiction** | Zone exposée où la règle générale est l'**interdiction de construire** | PPRN — zones rouges |


### Codes de zone (`CODEZONE`) sur les communes de la Plaine de la Crau 

| Code | Couleur | Définition |
|---|---|---|
| `R1` | 🔴 Rouge | Zones peu ou pas urbanisées (ZPPU) soumises à un **aléa modéré** (H ≤ 1 m) — inconstructibles sauf exceptions |
| `R2` | 🔴 Rouge | Zones peu ou pas urbanisées (ZPPU) **et** autres zones urbanisées (AZU) soumises à un **aléa fort** (H > 1 m) — inconstructibles sauf exceptions |
| `R2A` | 🔴 Rouge | Autres zones urbanisées à dominante d'**activités économiques** (industrielles, artisanales ou commerciales) en **aléa fort**,  |
| `RH` | 🔴 Rouge hachuré de jaune | **Bandes de sécurité** à l'arrière immédiat des ouvrages d'endiguement (digues, remblais routiers/ferroviaires, canaux…) où, en cas de **défaillance de l'ouvrage** (rupture ou surverse), l'aléa serait plus fort que l'inondation naturelle |
| `B1` | 🔵 Bleue | Zones de **centre urbain (CU)** et autres zones urbanisées (AZU) soumises à un **aléa modéré** — constructibles **sous prescriptions** |
| `B2` | 🔵 Bleue | Zones de **centre urbain (CU)** soumises à un **aléa fort** — constructibles **sous prescriptions** renforcées |
| `BR` | 🔵 Bleu clair | Zones comprises dans l'enveloppe de la **crue millénale** mais hors enveloppe de la zone inondable de l'aléa de référence (risque **résiduel**) |
| `P` | ⚪ Portuaire | **Site industrialo-portuaire (SIP)** — zonage particulier avec règles propres à l'activité portuaire |
| `ESM1` | **Espace Stratégique en cours de Mutation (ESM) en aléa modéré** — secteurs urbains en mutation (friches industrielles ou portuaires, secteurs de projets) où l'urbanisation peut être poursuivie sous prescriptions |
| `ESM2` | **Espace Stratégique en cours de Mutation (ESM) en aléa fort** — secteurs urbains en mutation (friches industrielles ou portuaires, secteurs de projets) où l'urbanisation peut être poursuivie sous prescriptions, mais soumis à un aléa fort : le règlement y est aligné sur celui d'une zone rouge d'aléa fort (type `R2`), très restrictif |
| `R` | Zone **rouge** — aléa fort, règle générale : **interdiction de construire** (sauf exceptions strictement encadrées par le règlement) |
| `B` | Zone **bleue** — aléa modéré, constructibilité admise **sous prescriptions** (matériaux insensibles à l'eau, réseaux étanches, etc.) |
| `BP` | **Bande de Précaution** à l'arrière des ouvrages de protection (digues, remblais) : secteur classé en **aléa très fort** du fait du **sur-aléa en cas de rupture ou surverse de l'ouvrage** (bande de sécurité de l'arrière-digue). Règle générale : inconstructibilité |

⚠️ La lecture d'un CODEZONE doit toujours se faire en regard du règlement local du PPR, qui seul définit sa valeur juridique 


---

## 📜 Conditions d'utilisation

- **Licence Ouverte / Open Licence version 2.0** ([texte de la licence](https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf)) ;
- Utilisation libre **sous réserve de citer la DDTM 13 comme source des données et d'indiquer la date de mise à jour** ;

> ⚠️ **Avertissement** : les données PPR ont un caractère réglementaire opposable ; la présente fiche est documentaire et ne se substitue pas aux documents officiels du PPR (rapport de présentation, règlement, zonage réglementaire consultables en préfecture ou sur le site de la DDTM 13 / Géorisques).