import os
import time
import requests
import pandas as pd

# --------------------------------------------------
# Configuration
# --------------------------------------------------

BASE_DIR = os.getenv(
    "PROJECT_BASE_DIR",
    "/content/drive/MyDrive/Satellite_Property_Valuation"
)

TRAIN_CSV = f"{BASE_DIR}/data/train(1)(train(1)).csv"
TEST_CSV  = f"{BASE_DIR}/data/test2(test(1)).csv"

IMAGE_DIR_TRAIN = f"{BASE_DIR}/train_images"
IMAGE_DIR_TEST  = f"{BASE_DIR}/test_images"

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")
if MAPBOX_API_KEY is None:
    raise ValueError("MAPBOX_API_KEY not set. Please set it as an environment variable.")

# --------------------------------------------------
# Functions
# --------------------------------------------------

def download_multi_zoom(lat, lon, base_path, zooms=(16, 17, 18)):
    """
    Download satellite images for multiple zoom levels.
    """
    for z in zooms:
        save_path = f"{base_path}_z{z}.png"

        # resume-safe
        if os.path.exists(save_path):
            continue

        url = (
            "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
            f"{lon},{lat},{z}/224x224"
            f"?access_token={MAPBOX_API_KEY}"
        )

        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            with open(save_path, "wb") as f:
                f.write(r.content)
        except Exception as e:
            print(f"Failed at {base_path}, zoom {z}: {e}")


def fetch_images(csv_path, image_dir, sleep_time=0.2):
    """
    Read CSV with lat/long and download satellite images.
    """
    os.makedirs(image_dir, exist_ok=True)
    df = pd.read_csv(csv_path)

    for i, row in df.iterrows():
        base_path = os.path.join(image_dir, str(i))

        # resume-safe marker
        if os.path.exists(f"{base_path}_z18.png"):
            continue

        download_multi_zoom(row["lat"], row["long"], base_path)
        time.sleep(sleep_time)

        if i % 100 == 0:
            print(f"Processed {i}")


# --------------------------------------------------
# Main execution
# --------------------------------------------------

def main():
    fetch_images(TRAIN_CSV, IMAGE_DIR_TRAIN)
    fetch_images(TEST_CSV, IMAGE_DIR_TEST)


if __name__ == "__main__":
    main()
