# Models Directory

This folder is designed to store the compiled Deep Learning models used by the Flask API for real-time inference. 

To keep the repository lightweight and to comply with GitHub's file size limits, large model files (such as `*.h5` and `*.keras`) are ignored by Git and will not be downloaded when you clone this repository.

### How to Run the API Locally:
For the `app.py` server to successfully launch, it requires the trained Champion model.
1. Run the model training pipeline located in the Jupyter Notebooks.
2. Export the final Multimodal Hybrid CNN-LSTM model.
3. Ensure the file is named `hybrid_cnn_lstm.keras` (or update the file path in `app.py` if you rename it).
4. Place the `.keras` file directly into this `models/` directory.
5. Launch the Flask server.
