# Machine Learning-Based Intrusion Detection System for Healthcare IoT Networks

## Overview

This project develops a Machine Learning-based Intrusion Detection System (IDS) for Healthcare Internet of Things (HIoT) environments.

The objective is to analyse network traffic behaviour and detect different cyber-attacks affecting IoT healthcare networks. Multiple machine learning models are developed and evaluated using different validation strategies to analyse performance, robustness, and generalisation capability.

The project evaluates models using:
 Internal validation, Stratified 5-fold cross-validation, External dataset validation,Mininet-based simulated network validation,Feature ablation analysis

The main focus of this project is to understand how well machine learning models perform when exposed to unseen network environments.

---

# Objectives

The main objectives of this project are:

Develop an ML-based IDS for Healthcare IoT networks,Detect normal and malicious network traffic patterns,Compare machine learning models for intrusion detection,Evaluate model reliability using multiple validation approaches,Analyse feature importance using ablation studies,Study model performance under domain shift using external and simulated datasets.

---

# Dataset

## Training Dataset

The primary dataset used for training and evaluation is:

**TON_IoT Network Dataset**

The dataset contains network traffic samples representing normal and attack activities.

The classification classes include:
Backdoor, DDoS, DoS, Injection, MITM, Normal,Password, Ransomware, Scanning, XSS

---

# Data Preprocessing

The same preprocessing pipeline was applied across all experiments.

## Data Cleaning

The following cleaning operations were performed:

- Missing values were replaced with `"unknown"`.
- "-" values were replaced with `"unknown"`.

---

## Feature Removal

The following features were removed:
Source IP address, Destination IP address, Source port, Destination port, SSL subject, SSL issuer, HTTP user agent, Original binary label column

### Reason for Feature Removal

These features were removed because:
IP addresses and port numbers are environment-dependent,They may introduce dataset-specific patterns, Removing them improves model generalisation to unseen networks, High-cardinality metadata features may not transfer effectively across different environments.

---

## Feature Transformation

### Categorical Features

Processed using:

- One-Hot Encoding
- Unknown category handling


### Numerical Features

Processed using:

- StandardScaler


The preprocessing pipeline was fitted only on training data and reused during validation to avoid data leakage.

---

# Machine Learning Models

Two machine learning algorithms were evaluated.

---

# Random Forest

Implementation:

`RandomForestClassifier`

Hyperparameters:

```python
n_estimators = 200
random_state = 42
n_jobs = -1
```

---

# XGBoost

Implementation:

`XGBClassifier`

Hyperparameters:

```python
n_estimators = 200
learning_rate = 0.1
random_state = 42
n_jobs = -1
objective = "multi:softprob"
eval_metric = "mlogloss"
```

---

# validation Design

The project consists of three major experimental files.

---

#  1: Training, Internal Validation, External Validation and Mininet Validation

## Internal Validation

The TON_IoT dataset was divided using stratified splitting:

```
90% Training Data
10% Internal Validation Data
```

The model was trained using the 90% training data and evaluated on the remaining unseen 10%.

Purpose:
Measure performance on unseen samples from the same dataset distribution, Evaluate baseline model performance.

---

## External Dataset Validation

After training, the model was evaluated on a completely unseen external dataset.

Purpose:
 Measure cross-dataset generalisation, Evaluate model robustness against different network traffic distributions.

---

## Mininet Validation

A simulated Healthcare IoT network environment was created using Mininet.

The trained models were evaluated using Mininet-generated network traffic.

generated from mininet through oracle virtial box and used zeek to convert the captures packets of .pcap file into .csv files 

running - python3 hiot_topoplogy.py
then combine the generated .pcap into csv merge_zeek.py
then the feature adptation is done to the genreated csv file  in 01_EDA.ipynb to produce mininet_processed.csv


Purpose:
Analyse performance under realistic simulated network conditions,Evaluate model behaviour under domain shift.

---

#  2: Stratified 5-Fold Cross Validation

A separate 5-fold cross-validation experiment was performed using the complete TON_IoT dataset.

For each fold:
The preprocessing pipeline was fitted only on the training fold.
The validation fold was transformed using the trained preprocessing pipeline.
The same machine learning models and hyperparameters were used.

Purpose:
Estimate model stability.
Reduce dependency on a single train-test split.
Measure consistency across different subsets of data.

---

#  3: Feature Ablation Study
AblationStudy_5fold.ipynb
An ablation study was performed to analyse the contribution of different network feature groups.

The following experiments were conducted:

---

## Baseline Model

Uses all available features.

---

## Without Traffic Features

Removed:
Duration, Source bytes, Destination bytes,Packet counts, IP byte statistics

Purpose:
Analyse the importance of traffic volume characteristics.

---

## Without Protocol Features

Removed:
Protocol, Service, Connection state

Purpose:
Analyse the contribution of communication-level features.

---

## Without Application Features

Removed:
 HTTP-related attributes

Purpose:
Evaluate the importance of application-layer information.

---

## Without DNS and SSL Features

Removed:
DNS features,SSL features

Purpose:
Analyse encrypted and domain-resolution-related information.

---

# Evaluation Metrics

The following evaluation metrics were used:

## Accuracy

Measures overall classification correctness.

## Precision

Measures the correctness of predicted attack classes.

## Recall

Measures the ability to identify actual attacks.

## Weighted F1 Score

Provides a balanced evaluation considering class distribution.

## Macro F1 Score

Measures performance equally across all classes.

---


# Running the Project

## 1. Model Training and Validation

Run:

```
Final_validation.ipynb
```

This performs:

- Data preprocessing
- 90/10 train-validation split
- Model training
- Internal validation
- External dataset validation
- Mininet validation  
- experminet in mininet_2a.ipynb

---

## 2. Cross Validation

Run:

```
5fold_crossValidation.ipynb
```

This performs:

- Stratified 5-fold cross-validation
- Performance stability analysis

---

## 3. Ablation Study

Run:

```
AblationStudy_5fold.ipynb
```

This performs:

- Feature group removal experiments
- Feature contribution analysis

---

# Technologies Used

## Programming Language

- Python

## Machine Learning Libraries

- Scikit-learn
- XGBoost

## Data Processing

- Pandas
- NumPy

## Network Simulation

- Mininet
- Zeek

## Visualisation

- Matplotlib
- Seaborn

---

# Key Outcomes

This project demonstrates:

- Machine learning models can effectively classify Healthcare IoT network attacks.
- Internal validation provides performance estimation on unseen samples from the same distribution.
- 5-fold cross-validation provides reliability and stability analysis.
- External validation evaluates cross-dataset generalisation.
- Mininet validation evaluates performance under simulated real-world network conditions.
- Ablation analysis identifies important network feature groups influencing intrusion detection performance.

---
 
 # other files in the folder are kept to show the experiments and different dataset that are captured through mininet 

# Author

**Kruthik Raj Manjunatha**

MSc Data Science  
Queen Mary University of London

---
# License

This project is developed for academic research purposes.