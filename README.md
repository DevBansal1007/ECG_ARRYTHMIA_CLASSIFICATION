# ECG Arrhythmia Classification & API Deployment
 
---
 
## 1. Project Overview
 
This repository contains a complete, end-to-end pipeline for **Electrocardiogram (ECG) arrhythmia classification** using the [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/). The primary objective is to develop a **"safety-first" diagnostic framework** that prioritizes the detection of life-threatening anomalies over simple global accuracy.
 
A major challenge in automated ECG analysis is the high morphological similarity between different beats, combined with **extreme class imbalance**. Traditional models often achieve high overall accuracy by defaulting to the majority "Normal" class, critically missing rare fatal arrhythmias like Fusion (F) and Ventricular (V) beats.
 
To solve this, we developed a **Multimodal Hybrid CNN-LSTM architecture**. By fusing raw 1D physical waveforms with handcrafted temporal markers (RR-intervals) and spectral frequencies (Discrete Wavelet Transform), this model successfully captures complex cardiac patterns. Finally, the Champion model is deployed via a **local Flask REST API**, demonstrating end-to-end MLOps capabilities from data ingestion to live clinical inference.
 
---
 
## 2. Repository Structure
 
```
ecg-arrhythmia-classification/
├── data/                    # Ignored by Git (Contains raw .dat and test .npy files)
├── models/                  # Ignored by Git (Contains hybrid_cnn_lstm.keras)
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   └── 02_model_training.ipynb
├── app.py                   # Flask API Server
├── test_api.py              # Client script for live clinical data injection
├── workflow_diagram.md
├── .gitignore               # Strict rules preventing data leakage to GitHub
├── README.md
└── requirements.txt
```
 
---
 
## 3. Key Results & Performance
 
The models were evaluated across five AAMI clinical classes: **Normal (N)**, **Supraventricular (S)**, **Ventricular (V)**, **Fusion (F)**, and **Unknown (Q)**.
 
### 🏆 Key Results
 
**1. Strong Overall Performance**
- Achieved an overall accuracy of **83.12%**
- Outperformed traditional ensemble models like XGBoost (80.7%)
**2. High Detection of Critical Arrhythmias**
- **Ventricular (V) Recall: 88.0%**
- Demonstrates strong capability in detecting life-threatening cardiac events
**3. Rare Class Detection Breakthrough**
- **Fusion (F) Recall: 19.0%**
- The only model capable of detecting this extremely rare class
- Significant improvement over baseline models (which had near-zero detection)
### 📊 Performance Summary
 
| Metric | Value |
|---|---|
| Overall Accuracy | 83.12% |
| Ventricular (V) Recall | 88.0% |
| Fusion (F) Recall | 19.0% |
 
---
 
## 4. Setup and Installation
 
To set up this project locally, follow these steps:
 
**Clone the repository:**
```bash
git clone https://github.com/your-username/ecg-arrhythmia-classifier.git
cd ecg-arrhythmia-classifier
```
 
**Create a virtual environment** (Python 3.11 recommended for TF compatibility):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
 
**Install the required libraries:**
```bash
pip install -r requirements.txt
```
 
---
 
## 5. Usage & Workflow
 
### 📌 Phase 1: Data Preprocessing
**`notebooks/01_data_preprocessing.ipynb`**
 
- Downloads the MIT-BIH records and extracts R-peaks
- Applies feature extraction: Raw Resampling, Handcrafted RR-intervals, db4 Wavelet Transforms
### 📌 Phase 2: Model Training
**`notebooks/02_model_training.ipynb`**
 
- Applies `GroupShuffleSplit` (strict patient-wise split to prevent data leakage)
- Uses **SMOTE** (Synthetic Minority Over-sampling) solely on training data
- Trains the Hybrid CNN-LSTM and baseline models
### 📌 Phase 3: MLOps & Local API Deployment
 
To transition from a static experiment to a functional software pipeline, the model is wrapped in a local Flask server for real-time inference.
 
**1. Start the Server:**
 
Place `hybrid_cnn_lstm.keras` in the `/models/` directory and start the Flask API:
```bash
python app.py
```
 
**2. Run the Clinical Test Suite:**
 
Place the preprocessed `X_test.npy` and `y_test.npy` in the `/data/` directory. Open a second terminal and trigger the inference script, which actively hunts for unseen patients across all 5 classes and transmits them as JSON payloads:
```bash
python test_api.py
```
 
---
 
## 6. Architecture Highlights
 
### 🧠 Algorithm: Multimodal Hybrid CNN-LSTM
 
| Component | Description |
|---|---|
| **CNN Branch** | Extracts spatial features and learns morphological patterns from the 360-sample ECG waveform |
| **LSTM Branch** | Captures temporal dependencies and models sequential rhythm patterns |
| **Feature Fusion** | Combines CNN + LSTM outputs, Handcrafted RR features, and Wavelet-based features into a final 379-feature vector |
| **Classification Layer** | Fully connected dense layers with Dropout regularization, outputting softmax probabilities across 5 classes |
 
---
 
## 7. MLOps Troubleshooting & Engineering Log
 
During the deployment of the Flask API, several critical architectural hurdles were resolved:
 
**Preventing Tensor Mismatch:** The model was engineered using the Keras Functional API. The Flask routing was customized to intercept the 1D JSON payload and slice it into three distinct NumPy arrays — `(1, 360, 1)`, `(1, 3)`, `(1, 16)` — to explicitly match the multi-branch input architecture.
 
**Physiological Edge Cases:** During API testing, the model flagged a normal (`N`) beat as Supraventricular (`S`). Clinically, this is an expected physiological overlap, as `S` beats share identical morphological shapes with `N` beats but differ temporally.
 
---
 
## 8. Data Source & Citation
 
This project uses the **MIT-BIH Arrhythmia Database** from PhysioNet.
 
> Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000).
> PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals.
> *Circulation*, 101(23), e215–e220.
 
---
 
## 9. Authors and Acknowledgements
 
- **Code Architect:** Dev Bansal
- **Data:** MIT-BIH Arrhythmia Database (PhysioNet) under the MIT License - see the [LICENSE](LICENSE) file for details.
