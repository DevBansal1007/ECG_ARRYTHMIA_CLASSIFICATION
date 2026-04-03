# Experimental Notebooks

This directory contains the core machine learning pipeline, originally developed and executed in Google Colab. The notebooks are structured sequentially to replicate the end-to-end workflow:

* **01_data_preprocessing.ipynb:** Raw MIT-BIH data extraction, AAMI mapping, multimodal feature engineering (waveforms, RR-intervals, Wavelets), execution of the master processing pipeline, and saving the final unified dataset prior to model training.
* **02_model_training.ipynb:** Implementation of strict patient-wise data splitting (`GroupShuffleSplit`) to prevent data leakage, application of SMOTE to handle class imbalance, training of baseline models (Logistic Regression, SVM, Random Forest, XGBoost), and the architecture construction, compilation, and training of the Multimodal Hybrid CNN-LSTM.
