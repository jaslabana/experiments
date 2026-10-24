"""Download Electric_Production.csv into data/.

1. Kaggle API (exact snapshot used in the notebook) - needs `pip install kaggle`
   and credentials in ~/.kaggle/kaggle.json
2. Fallback: FRED (original source, latest revision, trimmed to the same dates)
"""
from pathlib import Path
import shutil
import subprocess
import tempfile

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TARGET = DATA_DIR / "Electric_Production.csv"
KAGGLE_DATASET = "shenba/time-series-datasets"
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=IPG2211A2N"


def from_kaggle() -> bool:
    try:
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(
                ["kaggle", "datasets", "download", "-d", KAGGLE_DATASET,
                 "-f", "Electric_Production.csv", "-p", tmp, "--unzip"],
                check=True,
            )
            src = Path(tmp) / "Electric_Production.csv"
            if not src.exists():  # older CLI versions keep it zipped
                shutil.unpack_archive(next(Path(tmp).glob("*.zip")), tmp)
            shutil.copy(src, TARGET)
        print(f"Downloaded from Kaggle -> {TARGET}")
        return True
    except Exception as exc:
        print(f"Kaggle download failed ({exc}); falling back to FRED.")
        return False


def from_fred() -> None:
    df = pd.read_csv(FRED_URL)
    df.columns = ["DATE", "IPG2211A2N"]
    df["DATE"] = pd.to_datetime(df["DATE"])
    df = df[(df["DATE"] >= "1985-01-01") & (df["DATE"] <= "2018-01-01")]
    df.to_csv(TARGET, index=False, date_format="%m/%d/%Y")
    print(f"Downloaded from FRED ({len(df)} rows) -> {TARGET}")
    print("Note: FRED serves the latest revision, so values may differ slightly from Kaggle.")


if __name__ == "__main__":
    DATA_DIR.mkdir(exist_ok=True)
    if not from_kaggle():
        from_fred()
