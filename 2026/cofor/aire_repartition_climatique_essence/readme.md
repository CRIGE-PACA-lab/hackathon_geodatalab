# Utiliser un raster compressé (format cog.tif) sous Qgis  

## Généralités 

Le format Cloud Optimized GeoTIFF (COG) est un type de raster GeoTIFF spécialement conçu pour la diffusion web. 
Il est plus léger que le Geotiff classique et n'a **pas besoin d'être téléchargé** pour être exploité. 
Toutefois, en cas de mauvaise connexion, il peut tout à fait être téléchargé et charger en local comme un raster classique

## Mode d'emploi

### 1) Récupérer le lien du raster sous Github 

Par exemple, pour récupéré un MNT départemental à 5 mètres de résolution : 

	1. Entrer dans le dossier contenant sur le raster (.../rge_alti_5m) 
	2. Cliquer sur le raster souhaité (.../rge_alti_5m/rge_alti_5m_04_ass_cog.tif)
	3. Clic droit sur "View raw" : "copier le lien" (clic gauche pour télécharger)

![image_720](https://github.com/CRIGE-PACA-lab/hackathon_crige_2025/blob/main/img/image_720.png?raw=true)

### 2) Sous Qgis 

	1. Ouvrir Qgis 
	2. Couche 
	3. Ajouter une couche 
	4. Ajouter une couche raster 
	5. Type de source : selectionner "Protocole : HTTP(S),cloud, etc."
	6. Coller le lien du raster 
	7. Cliquer sur ajouter
	
**Vous pouvez désormais utiliser le raster comme un raster classique !**	

![image_721](https://github.com/CRIGE-PACA-lab/hackathon_crige_2025/blob/main/img/image_721.png?raw=true)

![image_722](https://github.com/CRIGE-PACA-lab/hackathon_crige_2025/blob/main/img/image_722.png?raw=true)
