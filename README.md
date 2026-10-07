# 🎓 Student Placement & Salary Prediction System

An end-to-end Machine Learning web application built using **Streamlit**, **Scikit-Learn**, and **Pandas**. This application predicts whether a student is likely to be placed based on academic performance, technical skills, and experience, and estimates their expected salary package (in LPA).

---

## 📌 Features

- **Placement Prediction:** Classification model (Logistic Regression) predicting whether a candidate will be placed.
- **Salary Estimation:** Regression model (Linear Regression) estimating the salary package in LPA for placed candidates.
- **Interactive UI:** User-friendly web interface powered by Streamlit for easy input of student attributes.
- **Comprehensive Feature Set:** Takes into account branch, college tier, CGPA, backlogs, technical skills (Coding, DSA, System Design, ML), and experience (internships, projects, hackathons).

---

## 🛠️ Tech Stack & Libraries Used

- **Language:** Python
- **Frontend / Web Framework:** Streamlit
- **Machine Learning & Preprocessing:** Scikit-Learn, Joblib
- **Data Analysis & Visualization:** Pandas, NumPy, Matplotlib, Seaborn

---

## 📊 Dataset & Model Details

- **Dataset Size:** 100,000 student records
- **Features (16 Input Attributes):**
  - **Academic:** Branch, College Tier, CGPA, Backlogs
  - **Skills:** Coding Skills, DSA Score, Aptitude Score, Communication Skills, ML Knowledge, System Design
  - **Experience:** Internships, Projects Count, Certifications, Hackathons, Open Source Contributions, Extracurriculars
- **Target Variables:**
  - `placement_status` (Classification: 0 or 1)
  - `salary_package_lpa` (Regression: Continuous Value)

---

## 📁 Project Structure

```text
├── app.py                      # Main Streamlit web application
├── student_placement.ipynb     # Jupyter Notebook for EDA, preprocessing, and model training
├── student_placement.csv       # Dataset used for training
├── placement_model.pkl         # Trained Logistic Regression classification model
├── salary_model.pkl            # Trained Linear Regression model
├── classification_scaler.pkl   # StandardScaler for classification input
├── regression_scaler.pkl       # StandardScaler for regression input
├── branch_encoder.pkl          # LabelEncoder for branch feature
├── tier_encoder.pkl            # LabelEncoder for college tier feature
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation

🚀 How to Run Locally1. Download / Clone the ProjectDownload the repository as a ZIP file from GitHub and extract it.2. Install DependenciesOpen your command prompt/terminal in the extracted folder and run:Bashpip install -r requirements.txt
Launch the Streamlit AppBashstreamlit run app.py
👤 Developer InfoDeveloper: Arya Anand Patil   Course: B.Sc. Data Science & Business Analysis   University: IT Vedant   
