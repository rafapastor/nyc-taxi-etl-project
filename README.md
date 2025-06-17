# 🗽 NYC Taxi ETL Project

Este proyecto implementa un pipeline **ETL (Extract, Transform, Load)** para procesar datos de viajes en taxi en la ciudad de Nueva York. El objetivo es limpiar y transformar los datos para generar un resumen estadístico diario útil para análisis posteriores.

## 📁 Estructura del proyecto

```
nyc-taxi-etl-project/
├── data/
│   ├── raw/                # Archivos originales descargados
│   ├── processed/          # Datos limpios en formato Parquet
│   └── output/             # Resultados en CSV
├── etl/
│   ├── extract.py          # Descarga de datos
│   ├── transform.py        # Limpieza y transformación
│   ├── load.py             # Carga y generación de resumen
│   └── run_pipeline.py     # Ejecuta el flujo ETL completo
├── main.py                 # Ejecuta el pipeline
└── README.md               # Este archivo
```

## ⚙️ Requisitos

- Python 3.8+
- pip
- Recomendado: entorno virtual (venv o conda)

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

## 🚀 Ejecución del pipeline

Ejecuta todo el flujo ETL con:

```bash
python main.py
```

Esto realizará automáticamente:

1. **Extracción:** descarga los datos desde una URL pública.
2. **Transformación:** limpia y enriquece los datos.
3. **Carga:** genera un resumen estadístico en CSV.

## 🔍 Descripción de cada etapa

### 1. `extract.py`

- Descarga un archivo `.parquet` y lo guarda en `data/raw/`.

### 2. `transform.py`

- Filtra columnas clave.
- Calcula la duración del viaje en minutos.
- Añade columnas: hora del día y día de la semana.
- Elimina registros inválidos.
- Guarda el resultado limpio en `data/processed/`.

### 3. `load.py`

- Agrupa los datos por fecha de recogida.
- Calcula:
  - duración media del viaje,
  - número total de viajes,
  - número medio de pasajeros.
- Redondea los valores a 4 decimales.
- Traduce los nombres de las columnas al español.
- Exporta el resumen como `data/output/trips_summary.csv`.

## 📊 Ejemplo del archivo final (`trips_summary.csv`)

| fecha_recogida | duracion_media_min | total_viajes | pasajeros_medios |
| -------------- | ------------------ | ------------ | ---------------- |
| 2021-01-01     | 12.4521            | 15321        | 1.2153           |
| 2021-01-02     | 14.7819            | 13244        | 1.1837           |

## 🧑‍💻 Autor

**Rafael Pastor García**

Proyecto personal para aprender y practicar procesos ETL con Python y Pandas.

## 📄 Licencia

MIT License
