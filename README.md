# Projet Big Data Docker

**Auteur :** Mohammed MOSLEH
**Date :** Janvier 2026

## Description
Ce dépôt contient une progression complète vers la mise en place d'une architecture Big Data conteneurisée. Du simple script de Data Science à un Cluster Spark distribué.

## Structure du projet

* **Exo 1 : Hello Data**
    * Conteneur Python simple.
    * Utilisation de **Pandas** pour la manipulation de DataFrames.

* **Exo 2 : Environnement Data Science**
    * Déploiement de **Jupyter Lab** via Docker.
    * Persistance des notebooks via volumes.
    * Accessible sur le port `8888`.

* **Exo 3 : Spark Local**
    * Introduction à **Apache Spark** (PySpark).
    * Exécution d'un job Spark en mode `local` (sans cluster).
    * Installation de Java (OpenJDK 11) dans le conteneur.

* **Exo 4 : Cluster Spark Distribué (Master/Worker)**
    * Architecture complète avec 3 services :
        1. **Spark Master** : Gestionnaire du cluster.
        2. **Spark Worker** : Nœud de calcul.
        3. **Spark Submit** : Conteneur client qui envoie le job au Master.
    * Résolution des conflits de versions (Python 3.8 / Java 11) pour la compatibilité stricte.

## Instructions de lancement

Chaque dossier contient un `Makefile` et un `docker-compose.yaml`.

**Pour lancer un exercice :**

```bash
cd exoX  # (Remplacer X par 1, 2, 3 ou 4)
make
# ou manuellement :
docker-compose up --build