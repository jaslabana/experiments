# Data

`Electric_Production.csv` — monthly US industrial production index for electric and gas utilities, January 1985 to January 2018.

| Column | Description |
|---|---|
| `DATE` | First day of the month |
| `IPG2211A2N` | Production index (renamed to `Electricity_Production` in the notebook) |

**Source**

- Kaggle: [Time Series Datasets (shenba)](https://www.kaggle.com/datasets/shenba/time-series-datasets?select=Electric_Production.csv)
- Original: Board of Governors of the Federal Reserve System (US), Industrial Production: Utilities: Electric and Gas Utilities, series [IPG2211A2N](https://fred.stlouisfed.org/series/IPG2211A2N), retrieved from FRED, Federal Reserve Bank of St. Louis.

**Re-downloading**

Run `python scripts/download_data.py`. It tries the Kaggle API first (needs a Kaggle account and `~/.kaggle/kaggle.json`), then falls back to FRED. The FRED version is the latest vintage, so values may differ slightly from the Kaggle snapshot because of revisions.
