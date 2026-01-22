from pyspark.sql import SparkSession

def run_spark_job():
    # 1. Initialiser la session Spark (le moteur)
    spark = SparkSession.builder \
        .appName("Exo3-Spark") \
        .master("local[*]") \
        .getOrCreate()
        
    # 2. Créer des données (Liste de tuples)
    data = [
        ("Alice", "Data Scientist", 5000),
        ("Bob", "DevOps", 4000),
        ("Charlie", "Data Engineer", 4500)
    ]
    columns = ["Nom", "Poste", "Salaire"]
    
    # 3. Créer un DataFrame Distribué
    df = spark.createDataFrame(data, columns)
    
    print("--- RESULTAT SPARK ---")
    # Afficher le contenu
    df.show()
    
    # Faire un petit calcul : moyenne des salaires
    print("Salaire moyen :")
    df.groupBy().avg("Salaire").show()
    print("----------------------")
    
    # 4. Arrêter Spark
    spark.stop()

if __name__ == "__main__":
    run_spark_job()