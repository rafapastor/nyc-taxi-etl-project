import os
import requests

def download_taxi_data(year: int, month: int, output_dir: str = "data/raw") -> str:
    filename = f"yellow_tripdata_{year}-{month:02d}.parquet"
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{filename}"
    output_path = os.path.join(output_dir, filename)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.exists(output_path):
        print(f"[INFO] File already exists: {output_path}")
        return output_path

    print(f"[INFO] Downloading {filename}...")
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"[INFO] Downloaded to: {output_path}")
    else:
        raise Exception(f"Failed to download file: {url}")

    return output_path
