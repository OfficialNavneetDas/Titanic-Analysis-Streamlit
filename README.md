# Titanic Survival Predictor & EDA Dashboard

This repository contains an end-to-end Data Science project that combines **Exploratory Data Analysis (EDA)** with **Machine Learning** to predict passenger survival on the Titanic. The application is built using **Streamlit**, providing an interactive interface for users to explore data and test survival scenarios in real-time.

## 🚀 Features

* **Interactive EDA:** Visualizations of passenger demographics, ticket classes, and survival correlations using Seaborn and Plotly.
* **Real-Time Prediction:** A "Board the Titanic" form where users can input personal details (Age, Sex, Class, Fare, etc.) to see if they would have survived the disaster.
* **Model Comparison:** The app utilizes three different trained classifiers to provide predictions:
    * **Naive Bayes:** For probabilistic classification.
    * **Support Vector Machine (SVM):** For effective high-dimensional boundary mapping.
    * **Random Forest:** For robust, ensemble-based decision making.
* **Data Preprocessing Pipeline:** Robust handling of missing values, categorical encoding, and feature scaling to ensure model accuracy.

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Streamlit
* **Data Libraries:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn

## 📦 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/OfficialNavneetDas/Titanic-Analysis-Streamlit.git](https://github.com/OfficialNavneetDas/Titanic-Analysis-Streamlit.git)
   cd Titanic-Analysis-Streamlit```
1. **Install dependencies::**
   ```bash
   pip install -r requirements.txt```
1. **Run the App:**
   ```bash
   streamlit run app.py```
   
## 📊 Dataset
The project uses the classic Titanic: Machine Learning from Disaster dataset from Kaggle, which includes information on the passengers' age, sex, sibling/spouse count, and embarkation point.
---
Developed as part of a Data Science portfolio.
Here is the clean Markdown code for your `README.md` file. You can copy and paste this directly into your VS Code editor.

```markdown
# Titanic Survival Predictor & EDA Dashboard

This repository contains an end-to-end Data Science project that combines **Exploratory Data Analysis (EDA)** with **Machine Learning** to predict passenger survival on the Titanic. The application is built using **Streamlit**, providing an interactive interface for users to explore data and test survival scenarios in real-time.

## 🚀 Features

* **Interactive EDA:** Visualizations of passenger demographics, ticket classes, and survival correlations using Seaborn and Plotly.
* **Real-Time Prediction:** A "Board the Titanic" form where users can input personal details (Age, Sex, Class, Fare, etc.) to see if they would have survived the disaster.
* **Model Comparison:** The app utilizes three different trained classifiers to provide predictions:
    * **Naive Bayes:** For probabilistic classification.
    * **Support Vector Machine (SVM):** For effective high-dimensional boundary mapping.
    * **Random Forest:** For robust, ensemble-based decision making.
* **Data Preprocessing Pipeline:** Robust handling of missing values, categorical encoding, and feature scaling to ensure model accuracy.

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Streamlit
* **Data Libraries:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn

## 📦 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/OfficialNavneetDas/Titanic-Analysis-Streamlit.git](https://github.com/OfficialNavneetDas/Titanic-Analysis-Streamlit.git)
   cd Titanic-Analysis-Streamlit
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App:**
   ```bash
   streamlit run app.py
   ```

## 📊 Dataset

The project uses the classic **Titanic: Machine Learning from Disaster** dataset from Kaggle, which includes information on the passengers' age, sex, sibling/spouse count, and embarkation point.

---
*Developed as part of a Data Science portfolio.*
```

---

### How to add this to your Repo:
1.  Open VS Code in your project folder.
2.  Create a new file named `README.md` (if you haven't already).
3.  Paste the code above into the file and save it.
4.  Run these commands to update your GitHub:
    ```bash
    git add README.md
    git commit -m "docs: add project description and setup instructions"
    git push origin main
    ```
