# 🧠 Employee Attrition Analysis and Prediction

Employee Attrition Analysis and Prediction is a Data Science project that uses machine learning models to analyze and predict key HR metrics. 
It focuses on predicting **employee attrition** using structured employee data.  
The project integrates data preprocessing, feature engineering, and model building, delivering insights through visualizations and metrics.

---

## 🔧 Tech Stack

![Python](https://img.shields.io/badge/Python-3.8%2B-gray?logo=python&logoColor=white&labelColor=3776AB)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-gray?logo=pandas&logoColor=white&labelColor=150458)
![Plotly](https://img.shields.io/badge/Plotly-Visualizations-gray?logo=plotly&logoColor=white&labelColor=11557c)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-gray?logo=numpy&logoColor=white&labelColor=013243)
![SciPy](https://img.shields.io/badge/SciPy-Statistical%20Analysis-gray?logo=scipy&logoColor=white&labelColor=8C5E9C)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-ML%20Models-gray?logo=scikit-learn&logoColor=white&labelColor=f89939)
![Google%20Colab](https://img.shields.io/badge/Google%20Colab-Notebook-gray?logo=google-colab&logoColor=white&labelColor=f9ab00)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-gray?logo=streamlit&logoColor=white&labelColor=FF4B4B)
![Power%20BI](https://img.shields.io/badge/Power%20BI-Business%20Dashboards-gray?logo=power-bi&logoColor=white&labelColor=F2C811)

---

## 📁 Project Structure

```
Project_3-Employee_Attrition_ML_Model/
├── 📁 app/
│   └── main.py                             # Streamlit app
├── 📁 dashboard/
│   └── HR_Attrition_Insights.pbix          # Power BI dashboard
├── 📁 dataset/
│   ├── employee_raw.csv                    # Raw dataset
│   └── employee_cleaned.csv                # Cleaned dataset
├── 📁 models/
│   └── logreg_pipeline_smote.pkl           # Trained ML models
├── 📁 notebooks/
|   ├── Employee_Attrition_Analysis.ipynb   # EDA & Model building (Colab)
│   └── ML_Model_Selection                  # Model Traning & Selection
├── 📁 notes/
|   ├──Preprocessing Guide.pdf              # Notes on preprocessing
│   └── Feature Selection.md                # Notes on Feature selection
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/wilson-in/Project_3-Employee_Attrition_Analysis_and_Prediction.git
   ```

2. Navigate to the project folder  
   ```bash
   cd Project_3-Employee_Attrition_Analysis_and_Prediction
   ```

3. Install required packages  
   ```bash
   pip install -r requirements.txt
   ```

4. Open the Jupyter Notebook to explore the project  
   ```bash
   jupyter notebook notebooks/Employee_Attrition_Analysis.ipynb
   ```

---

## 📊 Features

- Predict employee attrition risk based on HR features
- Data preprocessing and feature engineering pipeline
- Visualizations for better HR decision-making

---

## 📚 Sample Insights

- Employees with low job satisfaction and frequent overtime are more likely to leave
- High job involvement and tenure positively influence performance ratings
- Employees with strong historical ratings and tenure have higher promotion chances

---

