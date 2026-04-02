# ECG Arrhythmia Classification 

## 1. Project Overview

This repository contains a complete, end-to-end pipeline for Electrocardiogram (ECG) arrhythmia classification using the MIT-BIH Arrhythmia Database. The primary objective is to develop a "safety-first" diagnostic framework that prioritizes the detection of life-threatening anomalies over simple global accuracy.

A major challenge in automated ECG analysis is the high morphological similarity between different beats, combined with extreme class imbalance. Traditional models often achieve high overall accuracy by defaulting to the majority "Normal" class, critically missing rare fatal arrhythmias like **Fusion (F)** and **Ventricular (V) beats**.

To solve this, we developed a Multimodal Hybrid CNN-LSTM architecture. By fusing raw 1D physical waveforms with handcrafted temporal markers (RR-intervals) and spectral frequencies (Discrete Wavelet Transform), this model successfully captures complex cardiac patterns. Furthermore, this project utilizes a strict inter-patient data split, ensuring zero patient data leakage and proving the model's reliability on completely unseen patients.

---

## 2. Repository Structure
```
ecg-arrhythmia-classification/
├── data/
│   ├── raw/                  
│   └── processed/            
├── models/                   
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_baseline_ml_models.ipynb
│   └── 03_hybrid_dl_architecture.ipynb
├── workflow_diagram.md       
├── visuals/                  
├── .gitignore                
├── README.md                 
└── requirements.txt          
```

---
## 3. Key Results & Performance

The models were evaluated across **five AAMI clinical classes**:
- Normal (**N**)  
- Supraventricular (**S**)  
- Ventricular (**V**)  
- Fusion (**F**)  
- Unknown (**Q**)  

---

### 🏆 Key Results

#### 1. Strong Overall Performance
- Achieved an **overall accuracy of 83.12%**
- Outperformed traditional ensemble models like **XGBoost (80.7%)**

#### 2. High Detection of Critical Arrhythmias
- **Ventricular (V) Recall: 88.0%**
- Demonstrates strong capability in detecting **life-threatening cardiac events**

#### 3. Rare Class Detection Breakthrough
- **Fusion (F) Recall: 19.0%**
- The **only model** capable of detecting this extremely rare class  
- Significant improvement over baseline models (which had near-zero detection)

---

### 📊 Performance Summary

| Metric | Value |
|--------|------|
| **Overall Accuracy** | **83.12%** |
| **Ventricular (V) Recall** | **88.0%** |
| **Fusion (F) Recall** | **19.0%** |

---

### 🔍 Comparative Insight

| Model | Accuracy | Rare Class Detection |
|------|--------|---------------------|
| XGBoost | 80.7% | ❌ Poor |
| Random Forest | ~78% | ❌ Poor |
| Hybrid CNN-LSTM | **83.12%** | ✅ Strong |

---

## 4. Setup and Installation

To set up this project locally, follow these steps:

### Clone the repository:
```bash
git clone https://github.com/your-username/ecg-arrhythmia-classifier.git
cd ecg-arrhythmia-classifier
```

### Create a virtual environment (Recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install the required libraries:
```bash
pip install -r requirements.txt
```

## Compute Environment & Hardware

Due to the computational complexity of the Multimodal Hybrid CNN-LSTM, this project was developed and trained using **Google Colab** to leverage cloud-based hardware acceleration.

* **Compute:** Cloud-based GPU (NVIDIA T4 / Tesla P100)
* **Environment:** Google Colab Notebooks
* **Deep Learning Backend:** TensorFlow / Keras
  
## 5. Usage & Workflow
### 📌 Phase 1: Data Preprocessing
```bash
notebooks/01_data_preprocessing.ipynb

```
This step will:

- Download the **MIT-BIH records**
- Extract **R-peaks**
- Apply feature extraction methods:
  - Raw Resampling  
  - Handcrafted RR-intervals  
  - db4 Wavelet Transforms  

📁 **Output:** Saved as a unified `.npz` file
### Phase 2: Model Training & Evaluation
```bash
notebooks/02_model_training.ipynb
```
This step will:

- Apply **GroupShuffleSplit (patient-wise split)**
- Use **class weighting strategies**
- Train deep learning models  
- Automatically generate:
  - Evaluation metrics  
  - Confusion matrices  
  - ROC curves  
---
## 6. Architecture Highlights

### 🧠 Algorithm: Multimodal Hybrid CNN-LSTM

#### 🔹 CNN Branch
- Extracts **spatial features**  
- Learns morphological patterns from **360-sample ECG waveform**

#### 🔹 LSTM Branch
- Captures **temporal dependencies**  
- Models sequential rhythm patterns  

#### 🔹 Feature Fusion
- Combines:
  - CNN + LSTM outputs  
  - Handcrafted RR features  
  - Wavelet-based features  

➡️ **Final feature vector:** 379 features  

#### 🔹 Classification Layer
- Fully connected dense layers  
- Dropout regularization  
- Outputs **softmax probabilities** across 5 classes  
---

## 7. Data Source & Citation

This project uses the **MIT-BIH Arrhythmia Database** from PhysioNet.

> Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000).  
> *PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals.*  
> **Circulation**, 101(23), e215–e220.

---

## 8. Authors and Acknowledgements

- **Code Architect:** [Dev Bansal]
- **Data:** MIT-BIH Arrhythmia Database (PhysioNet)

---
## Workflow Architecture

For a detailed visual representation of the preprocessing pipeline, see the [Workflow Diagram](docs/workflow_diagram.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
