# Data 

This folder is intentionally left empty to keep the repository lightweight and to comply with GitHub's file size limits. The dataset used for this project is the **MIT-BIH Arrhythmia Database**.

## How to get the data:
1. Download the dataset from PhysioNet: https://physionet.org/content/mitdb/1.0.0/
2. Extract the downloaded files (`.dat`, `.hea`, `.atr`).
3. Place all the extracted files into the `data/raw/` directory.

## Processing the data:
Once the raw data is in place, run the preprocessing script. The generated NumPy arrays and engineered multimodal features (waveforms, timing, and wavelets) will automatically be saved to the `data/processed/` directory.
