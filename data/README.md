# Data 

This folder is intentionally left empty to keep the repository lightweight and to comply with GitHub's file size limits. The dataset used for this project is the **MIT-BIH Arrhythmia Database**.

## How to get the raw data:
1. Download the dataset from PhysioNet: https://physionet.org/content/mitdb/1.0.0/
2. Extract the downloaded files (`.dat`, `.hea`, `.atr`).
3. Place all the extracted files into the `data/raw/` directory.

## Testing the API locally:
If you are running the `app.py` Flask server and want to test it with real clinical data:
1. Run the Jupyter Notebooks to process the raw data and generate the final test arrays.
2. Locate the generated `X_test.npy` and `y_test.npy` files.
3. Place these two files **directly into this main `data/` directory** (do not put them in a subfolder).
4. Run `test_api.py` to trigger the local inference.
