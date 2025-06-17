import pandas as pd
import os

def load(input_path: str, output_path: str):
    print(f'Cargando datos limpios desde {input_path}...')
    df = pd.read_parquet(input_path)

    print('Generando resumen estadístico...')
    resumen = df.groupby(df['tpep_pickup_datetime'].dt.date).agg({
        'trip_duration_min': ['mean', 'count'],
        'passenger_count': 'mean'
    })

    # Aplanar MultiIndex columnas
    resumen.columns = ['_'.join(col) for col in resumen.columns]

    resumen["trip_duration_min_mean"] = resumen["trip_duration_min_mean"].round(3)
    resumen["passenger_count_mean"] = resumen["passenger_count_mean"].round(3)

    # Renombramos las columnas al español
    resumen = resumen.rename(columns={
        'trip_duration_min_mean': 'duracion_media_min',
        'trip_duration_min_count': 'total_viajes',
        'passenger_count_mean': 'pasajeros_medios'
    })
    resumen.index.name = 'fecha_recogida'  # 👉 cambia el nombre del índice

    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f'Guardando resumen en {output_path}...')
    resumen.to_csv(output_path)

    print('Carga finalizada y resumen guardado.')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python load.py <input_parquet> <output_csv>")
    else:
        load(sys.argv[1], sys.argv[2])
