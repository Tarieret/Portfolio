# Tariere A. Timitimi
## Data Science & ML Portfolio

Hi, my name is Tariere! 
I'm a ML Practitioner passionate about the end-to-end lifecycle of machine learning. My focus is on creating intelligent systems and deploying them efficiently in the cloud. I am constantly experimenting with new architectures and refining my approach to building impactful AI.

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
![Streamlit](/assets/img/Streamlitdemo.png)
- **Objective:** Build a Retrieval-Augmented Generation (RAG) system that enables question answering over custom PDF and text documents by combining embedding-based retrieval with grounded LLM responses.
- **Key Skills / Tech:** Python, LangChain, OpenAI API, Embeddings, Vector Databases, Document Chunking, Prompt Engineering, GenAI Systems
- **Repo:** [View Project](https://github.com/Tarieret/RAG-Based-Reseach-Assistant/blob/main/README.md)

### Financial Time-Series Forecasting: NVIDIA Case Study
This project was born out of a desire to understand exactly where classical forecasting fails in the face of high-market volatility. Using NVIDIA as a case study, I documented the breakdown of ARIMA models when confronted with exogenous shocks like the AI boom. By diagnosing these failures, specifically the violation of linear assumptions, I implemented a PyTorch based LSTM that captured the nonlinear dependencies ARIMA missed. This resulted in a significant improvement in error control (reducing MAE from 6.76 to 2.56) and reinforced the importance of choosing model architectures that match the underlying regime of the data.

**Key Skills/Tech:** Python, Time Series Analysis, ARIMA, MACD, LSTM (PyTorch), Deep Learning, RMSE / MAE, Model Evaluation, Failure Diagnosis
**Repo:** [View Project](https://github.com/Tarieret/Financial-Time-Series-Forecasting-NVIDIA-Case-Study)


### House Plant Health Classification Using Amazon Rekognition

- **Objective:** Build and deploy a houseplant health image classification workflow using Amazon Rekognition to detect plant health conditions (e.g., healthy vs. unhealthy, disease or stress indicators) from images, using a production-style pipeline for image ingestion, inference, and results storage.
- **Key Skills / Tech:** Python, Computer Vision, Amazon Rekognition (Labels and Custom Labels), Amazon S3, AWS Lambda, IAM, JSON parsing, Model Evaluation (Precision / Recall), Cloud Deployment
- **Repo:** *In Progress*

  
---

## 📂 Archived / Past Work 
Older projects and exploratory work are available in [Archived_Projects](https://github.com/Tarieret/Archived_Projects/tree/main) for reference.


---
## Certifications

<a href="https://www.credly.com" class="btn">AWS ML Engineer – Associate</a>, 
<a href="https://learn.nvidia.com" class="btn">NVIDIA Deep Learning</a>, 
<a href="https://credentials.databricks.com" class="btn">Databricks Fundamentals</a>, 
<a href="https://drive.google.com" class="btn">Databricks Apache Spark</a>, 
<a href="https://www.credly.com" class="btn">AWS Cloud Practitioner</a>



---
## Core Competencies

- **Methodologies:** Machine Learning, Deep Learning, Time Series Analysis, NLP, Big Data Analytics  
- **Languages:** Python (Pandas, NumPy, Scikit-Learn, Matplotlib), R (Dplyr, Tidyr, Caret, Ggplot2), SQL  
- **Tools & Platforms:** AWS SageMaker AI, S3, Lambda, Rekognition, MySQL, Tableau, Power BI, MS Excel  


<p align="center">
  <a href="mailto:tarieretimitimi@gmail.com" class="btn btn-primary">Email Me</a>
  <a href="https://www.linkedin.com" class="btn btn-info" style="background-color: #0a66c2; border-color: #0a66c2; color: white;">LinkedIn</a>
  
