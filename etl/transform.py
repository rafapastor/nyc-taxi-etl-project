import pandas as pd
import os

def transform_taxi_data(input_path: str, output_dir: str = "data/processed") -> str:
    print(f"[INFO] Loading file: {input_path}")
    df = pd.read_parquet(input_path)

    print("[INFO] Original columns:", df.columns.tolist())

    # Filtrar columnas clave
    columns_to_keep = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "passenger_count",
        "trip_distance",
        "PULocationID",
        "DOLocationID",
        "fare_amount"
    ]
    df = df[columns_to_keep]

    # Calcular duración del viaje (en minutos)
    df["pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    df["trip_duration_min"] = (df["dropoff_datetime"] - df["pickup_datetime"]).dt.total_seconds() / 60

    # Extraer hora y día de la semana
    df["hour"] = df["pickup_datetime"].dt.hour
    df["day_of_week"] = df["pickup_datetime"].dt.day_name()

    # Eliminar registros con duración o distancia negativas o nulas
    df = df[
        (df["trip_duration_min"] > 0) &
        (df["trip_distance"] > 0)
    ]

    # Guardar como Parquet limpio
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "yellow_tripdata_cleaned.parquet")
    df.to_parquet(output_file, index=False)

    print(f"[INFO] Saved cleaned data to: {output_file}")
    return output_file
