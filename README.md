# 🧠 Diabetes Prediction Using Machine Learning (KNN)

A web-based machine learning application built using **Django** that predicts the likelihood of a person having **Diabetes** based on medical attributes. The model is trained using the **K-Nearest Neighbors (KNN)** algorithm.

> 🔮 Designed to be clean, fast, and user-friendly with live prediction functionality.

---

## 🚀 Demo

![App UI Screenshot]
([https://github.com/sathishsathish31/Diabetes-Prediction_ML/blob/main/Screenshot%202025-06-22%20225308.png]),
([https://github.com/sathishsathish31/Diabetes-Prediction_ML/blob/main/Screenshot%202025-06-22%20225235.png])

**Live Demo:** *Coming Soon or Host Locally*

---

## 📌 Features

- 🔗 **Continuous Prediction** using trained KNN model
- 🧪 Input fields for 8 medical attributes
- 📊 Static Power BI dashboard for exploratory insights
- 🧠 KNN-based ML model integrated with Django
- 💡 Clean, modern UI with attractive gradient styling
- 🔒 CSRF-protected form submission

---

## 📂 Project Structure

MLProject/ ├── prediction/ │   ├── templates/ │   │   └── prediction/ │   │       └── predict.html │   ├── static/ │   │   └── prediction/ │   │       └── css/ │   │           └── styles.css │   ├── knn_model.pkl │   └── views.py ├── MLProject/ │   └── settings.py ├── manage.py └── requirements.txt

---

## 📊 Features Used for Prediction

- `Pregnancies`
- `Glucose`
- `Blood Pressure`
- `Skin Thickness`
- `Insulin`
- `BBI`
- `Diabetes Pedigree Function`
- `Age`

➡️ **Target Variable:** `Outcome` (0 = Non-diabetic, 1 = Diabetic)

---

## ⚙️ Technologies Used

- 🐍 Python
- ⚙️ Django (Backend Framework)
- 🤖 scikit-learn (KNN ML Model)
- 💾 Pickle (for saving/loading model)
- 🌐 HTML5 / CSS3
- 📈 Seaborn & Matplotlib (Visualization)

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/Diabetes-Prediction-ML.git
cd Diabetes-Prediction-ML

# Create and activate virtual environment
python -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

Then go to http://127.0.0.1:8000//prediction to use the app.


---

📁 Deployment

You can deploy this project on platforms like:

Render

PythonAnywhere

Vercel (for static UI)


Need help deploying? Just ask!

---
## 📓 Jupyter Notebook

The complete process of data preprocessing, EDA (exploratory data analysis), and training the KNN model is documented in the Jupyter Notebook.

📁 File included: [https://github.com/sathishsathish31/Diabetes-Prediction_ML/blob/main/knn_model.ipynb]

### Contents:
- 🔍 Data Cleaning
- 📊 Visualizations (Seaborn & Matplotlib
---

## 📈 Visualization Examples

The project includes data visualization using Seaborn and Matplotlib such as:

- Correlation Heatmap
- Outcome Distribution
- Feature-wise distribution (e.g., Glucose vs Outcome)
  
These plots are rendered inside Django views or as static images in templates


---

🙌 Author

Sathees kumar K
Final Year B.Sc. CS Student | Data Analyst & Developer Enthusiast
GitHub:[https://github.com/sathishsathish31]  | Linkedin :[https://www.linkedin.com/in/sathees-kumar-k-23b3aa354]


---

⭐️ Show Your Support

If you like this project:

⭐ Star the repository

🍴 Fork it

🐛 Report issues or suggest features!



---

⭐️ Show Your Support

Give a ⭐️ if you like this project

Share with others in the Data science ,Data Analytics, ML  and Django community!


---

Let me know if you'd like:
- A `requirements.txt` auto-generated
- Help rendering Matplotlib images in Django
- A custom GitHub cover image for your repo

You're nearly there to show this off on LinkedIn!
