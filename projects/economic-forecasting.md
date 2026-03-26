---
layout: page
title: Economic Time-Series Forecasting on AWS SageMaker
subtitle: XGBoost vs ARIMA vs Prophet — deployed end-to-end on AWS SageMaker
---

**[← Back to Portfolio](https://tarieret.github.io/Portfolio/)**

---

## Overview

This project forecasts U.S. Consumer Price Index (CPI) values using a multi-model approach, ranging from classical statistical methods to gradient boosting. The primary objective was to evaluate model accuracy under a rigorous time-series validation framework and demonstrate production-level deployment on AWS SageMaker.

A key decision mid-project was pivoting away from LSTM after testing showed deep learning struggled with the small monthly sample size and non-stationary trend of CPI data — a deliberate architectural choice in favor of a more robust tree-based approach.

![XGBoost CPI Forecast](/Portfolio/assets/img/RMSE_Comparison.png)
![XGBoost CPI Forecast](/Portfolio/assets/img/XGBoost_CPI.png)

---

## Results

Performance evaluated on a 24-month holdout set (Dec 2023 – Nov 2025):

| Model | MAE | RMSE |
|-------|-----|------|
| **XGBoost (Winner)** | **1.83** | **2.0** |
| Prophet | 7.09 | 7.15 |
| ARIMA (1,1,1) | 8.04 | 9.29 |

---

## Data

- **Source:** Federal Reserve Economic Data (FRED)
- **Series:** CPIAUCSL (Monthly)
- **Evaluation window:** 24-month holdout

---

## Technical Approach

- Applied first-order differencing to remove trend bias — model predicts monthly delta rather than absolute CPI values
- Engineered a 12-month sliding window of lag features to capture seasonal momentum and annual cycles
- Benchmarked ARIMA and Prophet as statistical baselines before training XGBoost
- Serialized the final model into `model.tar.gz` with a custom inference handler for SageMaker deployment
- Deployment script intentionally separated from the notebook to avoid unnecessary cloud costs

---

## Tech Stack

`Python` `XGBoost` `ARIMA` `Prophet` `AWS SageMaker` `Boto3` `Pandas` `Scikit-learn` `FRED API` `MLOps`

---

**[View Full Repo on GitHub](https://github.com/Tarieret/Economic-Time-Series-Forecasting-on-AWS-SageMaker)** · **[Back to Portfolio](https://tarieret.github.io/Portfolio/)**
