import subprocess

def run():
    print("1. Extrayendo datos...")
    subprocess.run(["python", "etl/extract.py"], check=True)

    print("\n2. Transformando datos...")
    subprocess.run([
        "python", "etl/transform.py",
        "data/raw/yellow_tripdata_2023-01.parquet",
        "data/processed/yellow_tripdata_cleaned.parquet"
    ], check=True)

    print("\n3. Cargando datos y generando resumen...")
    subprocess.run([
        "python", "etl/load.py",
        "data/processed/yellow_tripdata_cleaned.parquet",
        "data/output/trips_summary.csv"
    ], check=True)

    print("\nPipeline completo. Resumen guardado en data/output/trips_summary.csv")

if __name__ == "__main__":
    run()
