import time
from pyspark.sql import SparkSession

def run_cluster_job():
    print("--- ATTENTE DU DEMARRAGE DU CLUSTER (10s) ---")
    time.sleep(10) # On laisse le temps au Master/Worker de s'allumer

    print("--- CONNEXION AU MASTER ---")
    # On se connecte à l'URL du conteneur 'spark-master' sur le port 7077
    spark = SparkSession.builder \
        .appName("Exo4-Cluster") \
        .master("spark://spark-master:7077") \
        .getOrCreate()
        
    data = [("Cluster", "Master", 1), ("Cluster", "Worker", 2)]
    df = spark.createDataFrame(data, ["Type", "Role", "ID"])
    
    print("--- RESULTAT DU CLUSTER ---")
    df.show()
    
    # Un calcul un peu lourd pour faire travailler le Worker
    print("Calcul distribué (création de 1000 lignes)...")
    spark.range(1000).groupBy().count().show()
    
    spark.stop()

if __name__ == "__main__":
    run_cluster_job()