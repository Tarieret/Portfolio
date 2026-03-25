## Data Science & ML Portfolio

Hi, my name is Tariere! 
I'm a ML Practitioner passionate about the end-to-end lifecycle of machine learning.My focus is on building end-to-end ML systems: from exploratory analysis and model selection to cloud deployment, with an emphasis on making deliberate, well-reasoned architectural decisions. I am constantly experimenting with new architectures and refining my approach to building impactful AI.

✨ Interests: Artist, lifelong learner, and fan of great books and better company.

**Technical Skills:**  Python, R, SQL, Machine Learning, Deep Learning, AWS 

---

## Featured Projects

### Economic Time-Series Forecasting on AWS SageMaker
![XGBoost CPI Forecast](/assets/img/XGBoost_CPI.png)
I built this project to explore how different machine learning architectures handle the nuances of U.S. macroeconomic data. After benchmarking classical statistical models against modern gradient boosting, I found that XGBoost, paired with a 12-month lookback window and stationarity transformations,far outperformed traditional methods like ARIMA. A major part of the journey was the decision to pivot away from Deep Learning (LSTM) when it became clear the architecture wasn't suited for the specific scale of this dataset. To bridge the gap between development and production, I structured the final model to be compatible with AWS SageMaker, including a custom inference handler for scalable cloud hosting.

**Key Skills/Tech:** Python, XGboost, ARIMA, Prophet, SageMaker AI, Cloud Deployment, MLOps      
**Repo:** [View Project](https://github.com/Tarieret/Economic-Time-Series-Forecasting-on-AWS-SageMaker)


### RAG-Based Research Assistant
![Streamlit](/assets/img/StreamlitDemo1.png)
This project explores how Retrieval-Augmented Generation can make domain-specific medical research easier to work with. It ingests peer-reviewed papers on brain tumor detection, indexes them using semantic embeddings, and returns citation backed answers through a FastAPI backend and a Streamlit interface. The idea for a research assistant came out of a Spring 2025 master’s-level project on data mining and deep learning for brain tumor detection from MRI images, which pushed me to think less about individual models and more about supporting the research workflow itself. A key focus here was building a RAG pipeline that is accurate, responsive, and usable by multiple users, while still being simple enough to run locally. The original MRI classification project can also be found in my archived projects [here](https://github.com/Tarieret/Archived_Projects/tree/main/Brain_Tumor_Classification).

**Key Skills/Tech:** Python, FastAPI, OpenAI API, LangChain, ChromaDB, Streamlit, Retrieval-Augmented Generation

**Repo:** [View Project](https://github.com/Tarieret/RAG-Based-Reseach-Assistant/blob/main/README.md)



### House Plant Health Classification Using Amazon Rekognition
![storefront](assets/img/storefront.png)
For this project, I wanted to build an end-to-end houseplant health classification pipeline using Amazon Rekognition Custom Labels. Starting with 91 personal houseplant photos, the pipeline handles class imbalance through targeted image augmentation, splits data with stratification, and uploads labeled training images to S3 via manifest files. A Rekognition Custom Labels model was trained on the augmented dataset and evaluated against a test set, achieving 95% accuracy with a precision of 1.00 and recall of 0.80 on the minority unhealthy class. 

The project goes beyond model training by deploying a serverless inference pipeline using AWS Lambda, which automatically triggers on new S3 uploads, runs inference, saves results as JSON, and stops the model to avoid unnecessary charges. Every AWS resource (S3, Rekognition, Lambda, and IAM) was provisioned and managed entirely through Python, making the pipeline fully reproducible from a single notebook

A big thank you to the staff at Holiday Foliage Orchids and Plants (146 W 28th St, NYC) and Redwood Flower Shop (New Brunswick, NJ) for letting me walk around and photograph their plants. Couldn't have built this dataset without them!

**Dataset:** Available on Kaggle@ [Houseplant Health Classification Dataset](https://www.kaggle.com/datasets/tarieretimitimi/houseplant-health-classification-dataset)

**Key Skills/Tech:** Python, Amazon Rekognition, Custom Labels, Amazon S3, AWS Lambda, IAM, boto3, Albumentations, scikit-learn, Model Evaluation (Precision/Recall/F1)

**Repo:** [View Project](https://github.com/Tarieret/Houseplant-Health-Classification)



### Film Industry EDA (SQL & R)
![Top Genres](/assets/img/02_top_genres.png)
I built this project to analyze patterns across 60,000+ films using a production-style data pipeline, loading raw TMDB data into a SQLite database, querying it with SQL, and wrangling and visualizing the results in R. A key early decision was dropping financial analysis entirely after discovering that fewer than 17,000 of 1.38 million entries had both budget and revenue recorded but not enough to draw meaningful conclusions. Instead, the analysis focuses on genre trends, audience ratings, and popularity patterns across four decades of cinema. Two findings stood out: popularity and rating are essentially uncorrelated (r = 0.087), suggesting commercial reach and perceived quality are largely independent, and Drama movies consistently outrate Action films (6.27 vs. 5.96), a statistically significant gap across 35,000+ films.

**Key Skills / Tech:** R, tidyverse, ggplot2, lubridate, ggrepel, SQLite, DBI, RSQLite, Exploratory Data Analysis, Data Wrangling, Statistical Analysis (Correlation, Hypothesis Testing), Data Visualization

**Repo:** [View Project](https://github.com/Tarieret/Film-Industry-EDA)


### Financial Time-Series Forecasting: NVIDIA Case Study

- **Objective:** Investigate the limitations of classical time-series models under high-volatility market conditions using NVIDIA stock as a case study. The project diagnoses ARIMA failure modes — including stationarity violations and linear assumption breakdown during the AI boom — and implements a PyTorch-based LSTM as a nonlinear alternative, with full model evaluation and diagnostic analysis.
- **Key Skills / Tech:** Python, Time Series Analysis, ARIMA, ARIMAX, MACD, Stationarity Testing (ADF/KPSS), Ljung-Box Diagnostics, LSTM (PyTorch), Deep Learning, RMSE / MAE / R², Model Evaluation, Failure Diagnosis
- **Repo:** *In Progress*
 
---

## 📂 Archived / Past Work 
Older projects and exploratory work are available in [Archived_Projects](https://github.com/Tarieret/Archived_Projects/tree/main) for reference.


---
## Certifications

<a href="https://www.credly.com/badges/8983ce52-d5b0-421a-b7c5-80b3e9fa676f/linked_in_profile" class="btn">AWS ML Engineer – Associate</a>, 
<a href="https://www.nvidia.com/en-us/training/" class="btn">NVIDIA Deep Learning</a>, 
<a href="https://credentials.databricks.com/c6b25acf-076b-494f-a959-740542fa0033#acc.PeisynNm" class="btn">Databricks Fundamentals</a>, 
<a href="https://drive.google.com/file/d/1LnDWoYYBcAIY72g8Dj0FVGfU1gluaUSr/view" class="btn">Databricks Apache Spark</a>, 
<a href="https://www.credly.com/badges/4881e30a-e6a7-4906-8342-364b621a6b59/linked_in_profile" class="btn">AWS Cloud Practitioner</a>



---
## Core Competencies

- **Methodologies:** Machine Learning, Deep Learning, Time Series Analysis, NLP, Big Data Analytics  
- **Languages:** Python (NumPy, Pandas, Matplotlib, Scikit-Learn, PyTorch), R (Dplyr, Tidyr, Caret, Ggplot2), SQL  
- **Tools & Platforms:** AWS SageMaker AI, S3, Lambda, Rekognition, MySQL, SQLite, Tableau, Power BI, MS Excel  


<p align="center">
  <a href="mailto:tarieretimitimi@gmail.com" class="btn btn-primary">Email Me</a>
  <a href="https://www.linkedin.com/in/tariere-timitimi/" class="btn btn-info" style="background-color: #0a66c2; border-color: #0a66c2; color: white;">LinkedIn</a>
  
