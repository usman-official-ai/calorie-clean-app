# AI-Powered Calorie Burn Predictor  
**Deployment**  

  🚀 **Live App:** [Click here to open Calorie Burn App](https://calorie-clean-app-kfuukhf3zmexzeu86yfibq.streamlit.app)  
    
<img width="1402" height="1122" alt="Image" src="https://github.com/user-attachments/assets/4e2223ac-e796-492c-be3d-426e59fff751" />

A production-ready intelligent system that predicts calories burned from natural language workout descriptions using **Random Forest** and **Google Gemini LLM**. Built with **Streamlit** for interactive deployment.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Model Performance](#model-performance)
- [Sample Input / Output](#sample-input--output)
- [AI Automation](#ai-automation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Live Demo](#live-demo)
- [Author](#author)
- [License](#license)

---

## Overview

This project bridges **traditional machine learning** with **generative AI**. Users describe their workout in natural language (e.g., *"I am 22, male, 175cm, 68kg, cycled 35 min, heart rate 145"*). The Gemini LLM extracts structured features, which are fed into a trained Random Forest model to predict calories burned. An automated pipeline ensures data validation, performance monitoring, and retraining readiness.

---

## Key Features

- **Natural Language Interface** – No forms, just describe your workout.
- **LLM-Powered Feature Extraction** – Gemini 2.5 Flash extracts Age, Gender, Height, Weight, Duration, Heart Rate.
- **ML-Based Prediction** – Random Forest Regressor with R² > 0.95.
- **Auto Data Validation** – Detects missing values, duplicates, and outliers before inference.
- **Auto Performance Monitoring** – Tracks MAE in real time and alerts when retraining is needed.
- **Feature Engineering** – Dynamically computes BMI from height/weight.
- **Interactive Web App** – Streamlit frontend with one-click prediction.

---

## Tech Stack

| Area | Technology |  
|------|------------|  
| Language | Python 3.12 |  
| ML Framework | Scikit-learn (Random Forest) |  
| LLM | Google Gemini 2.5 Flash |  
| Web App | Streamlit |  
| Data Processing | Pandas, NumPy |  
| Visualization | Matplotlib, Seaborn |  
| Version Control | Git / GitHub |  
| Deployment | Streamlit Cloud |  

---

## Project Structure  
calorie-clean-app/  
├── app.py # Streamlit application  
├── calorie_model.pkl # Trained Random Forest model  
├── scaler.pkl # StandardScaler for feature scaling  
├── label_encoder.pkl # LabelEncoder for gender  
├── requirements.txt # Python dependencies  
├── README.md # Project documentation  
└── .streamlit/  
└── secrets.toml # API keys (excluded from public repo)  
   
text  

---

## Installation & Setup  

### 1. Clone the repository  

```bash
git clone https://github.com/usman-official-ai/calorie-clean-app.git
cd calorie-clean-app  
2. Create a virtual environment (recommended)  
bash  
python -m venv venv  
source venv/bin/activate      # Linux/Mac  
venv\Scripts\activate          # Windows  
3. Install dependencies  
bash  
pip install -r requirements.txt  
4. Set up Gemini API key  
Create .streamlit/secrets.toml:  

toml  
GEMINI_API_KEY = "your_google_gemini_api_key_here"
Obtain your free API key from Google AI Studio

5. Run the application
bash
streamlit run app.py
Access the app at http://localhost:8501

Model Performance
Metric	Value
Algorithm	Random Forest Regressor
R² Score	0.95
Mean Absolute Error (MAE)	~12 calories
Root Mean Squared Error (RMSE)	~18 calories
Training Features	Age, Gender, Height, Weight, Duration, Heart Rate, BMI
Training Samples	15,000 (after cleaning)
Feature Importance (Normalized)
Feature	Importance
Duration	0.42
Heart Rate	0.23
BMI	0.15
Age	0.09
Weight	0.06
Height	0.03
Gender	0.02
Sample Input / Output
Input (Natural Language)
text
I am 22 years old male, height 175 cm, weight 68 kg. I cycled for 35 minutes and my heart rate was 145 bpm.
Output
json
{
  "Predicted Calories": 236.4,
  "Extracted Features": {
    "Age": 22,
    "Gender": "Male",
    "Height": 175,
    "Weight": 68,
    "Duration": 35,
    "Heart_Rate": 145
  }
}
AI Automation
This project includes three levels of automation:

Module	Description
Auto Data Validation	Validates input data for missing values, duplicates, and outliers before prediction. Alerts on failures.
Auto Performance Monitoring	Continuously evaluates model MAE against a threshold (35 kcal). Triggers alert when performance degrades.
Auto Retraining	Framework-ready function to retrain the model on new data. Can be scheduled via GitHub Actions or cron.
These automation features demonstrate MLOps readiness for production environments.

Exploratory Data Analysis
The training pipeline includes the following visualizations:

Distribution of calories burned (histogram + KDE)

Correlation heatmap of all numeric features

Calories vs Duration scatter plot (colored by gender)

Calories vs Heart Rate scatter plot

Feature importance bar chart

These help in understanding feature relationships and model interpretability.

Live Demo
Note: The live demo requires a valid Gemini API key and may not be always active due to free tier limits.

https://calorie-clean-app-usman-official-ai.streamlit.app

Author
 usman-official-ai

License
This project is released under the MIT License for educational and portfolio purposes.

Show Your Support
If you find this project useful, please consider:

⭐ Starring the repository on GitHub

🔗 Sharing it on LinkedIn or other platforms

📧 Reaching out for collaboration or feedback

Built with Python, Streamlit, Scikit-learn, and Google Gemini.


