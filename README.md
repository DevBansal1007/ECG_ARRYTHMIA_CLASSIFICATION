# ECG Arrhythmia Classification - Phase 1: Preprocessing

## 1. Project Overview

This repository contains the complete data processing and feature extraction pipeline (Phase 1) for an advanced ECG-based arrhythmia classification project. The primary goal of this project is to build a deep learning model capable of accurately classifying heartbeat anomalies.

A key challenge in this domain is the high morphological similarity between certain beat types, such as:

- **Normal (N)** and **Supraventricular Ectopic (S)** beats
- **Ventricular Ectopic (V)** and **Fusion (F)** beats

This preprocessing phase is designed to load, segment, and transform raw ECG signals into multiple feature-rich formats, providing a robust foundation for building and testing advanced classification models (like hybrid CNN-LSTMs) in Phase 2.

---

## 2. Repository Structure
```
ecg-arrhythmia-classifier/
│
├── .gitignore                 # Tells Git which files to ignore
├── LICENSE                    # Project license (MIT)
├── README.md                  # This file
├── requirements.txt           # Python libraries needed to run the code
│
├── docs/
│   ├── report.html            # Detailed HTML report of the workflow
│   ├── workflow_diagram.md    # Mermaid code for the architecture diagram
│   └── images/                # Images for the HTML report
│
├── notebooks/
   └── 01_preprocessing.ipynb # Interactive Jupyter notebook with visualizations
```

---

## 3. Setup and Installation

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

---

## 4. How to Run the Preprocessing

### Option A: Using Jupyter Notebook (Interactive)

1. Launch Jupyter:
```bash
   jupyter notebook
```

2. Open `notebooks/ecg-preprocessing-work.ipynb`

3. Run all cells or execute step-by-step

This will:

- Download record '100' from the MIT-BIH database
- Filter, segment, and process all 'N' (Normal) beats
- Perform all three feature extraction methods
- Save all 7 plots (e.g., `plot_step1_raw_signal.png`, `plot_step3_method1_resample.png`, etc.) into a folder named `report_images/`

---

## 5. Detailed Report

   A full, interactive HTML report describing the entire workflow, comparing the three feature extraction methods, and visualizing the data is available.

   **View the live report here:** [ECG Preprocessing Report](https://devbansal1007.github.io/ECG_ARRYTHMIA_CLASSIFICATION/report.html) 

---

## 6. Data Source

This project uses the **MIT-BIH Arrhythmia Database**. This data is provided by PhysioNet and must be cited correctly.

### Citation:

> Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. *Circulation* [Online]. 101 (23), pp. e215–e220.

---

## 7. Phase 2: Future Work

This repository (Phase 1) successfully prepares the data. The next phase of the project will focus on:

- **Full Dataset Processing:** Scaling the `01_preprocessing.py` script to process all 48 records from the MIT-BIH database
- **Class Imbalance:** Implementing strategies (e.g., SMOTE, class weights) to handle the severe class imbalance
- **Model Development:** Building a hybrid CNN-LSTM model that uses a multi-input architecture (Method 1 + Method 2 features)
- **Training & Evaluation:** Training the model and using advanced metrics (F1-score, Precision, Recall, Confusion Matrix) to evaluate its performance, especially on the difficult 'S' and 'F' classes

---

## 8. Authors and Acknowledgements

- **Code Architect:** [Dev Bansal]
- **Data:** MIT-BIH Arrhythmia Database (PhysioNet)

---
## Workflow Architecture

For a detailed visual representation of the preprocessing pipeline, see the [Workflow Diagram](docs/workflow_diagram.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
