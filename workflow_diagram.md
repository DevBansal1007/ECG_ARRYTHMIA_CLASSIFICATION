# Project Workflow Architecture

The following diagram illustrates the end-to-end pipeline, from raw clinical data ingestion to final comparative evaluation.

```mermaid
graph TD
    %% Data Ingestion & Preprocessing
    A[(Raw MIT-BIH Database)] --> B[AAMI Super-class Mapping]
    B --> C[Signal Segmentation & R-Peak Centering]
    
    %% Multimodal Feature Extraction
    C --> D{Multimodal Extraction}
    D -->|Method 1| E[Raw Resampled Waveforms]
    D -->|Method 2| F[Handcrafted Timing RR-Intervals]
    D -->|Method 3| G[db4 Wavelet Transform Statistics]
    
    %% Data Fusion & Splitting
    E --> H[Early Feature Fusion]
    F --> H
    G --> H
    H --> I{Strict Patient-Wise Split<br/>GroupShuffleSplit}
    
    %% Training Pipeline
    I -->|80% Training Patients| J[Training Set]
    I -->|20% Unseen Patients| K[Test Set]
    J --> L[SMOTE Class Balancing]
    L --> M((Proposed Hybrid CNN-LSTM))
    L --> N[Baseline Models: SVM, RF, XGBoost]
    
    %% Evaluation
    M --> O{Comparative Evaluation}
    N --> O
    K --> O
    O --> P[Multi-Class ROC Curves]
    O --> Q[Confusion Matrices]
    O --> R[Precision, Recall & F1-Scores]
    
    %% Styling (Fixed for Dark Mode visibility)
    classDef database fill:#f9f,stroke:#333,stroke-width:2px,color:#000;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px,color:#000;
    classDef model fill:#dfd,stroke:#333,stroke-width:4px,color:#000;
    
    class A database;
    class B,C,E,F,G,H,I,L process;
    class M model;
