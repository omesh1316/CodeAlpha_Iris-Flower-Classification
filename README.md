# 🌸 Iris Flower Classification using Machine Learning

This project is a simple Machine Learning application that classifies Iris flowers into three species — **Setosa**, **Versicolor**, and **Virginica** — based on their physical measurements.

The project uses **Scikit-learn** for model training and **Streamlit** to build an interactive web interface.

---

## 📌 Features
- Uses Iris flower measurements as input:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- Trains a Machine Learning classification model
- Predicts Iris species in real-time
- Interactive web UI built with Streamlit
- Clean and modular project structure

---

## 🛠️ Technologies Used
- Python
- Scikit-learn
- Streamlit
- NumPy
- Pandas

---

## 📂 Project Structure
Iris-Flower-Classification/
│
├── app.py
├── requirements.txt
├── README.md
│
└── src/
├── data_loader.py
├── model.py
└── evaluate.py


---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/omesh1316/CodeAlpha_Iris-Flower-Classification.git
cd CodeAlpha_Iris-Flower-Classification

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
python -m streamlit run app.py

The application will open in your browser at:
http://localhost:8501

📊 Model Details

Algorithm Used: Logistic Regression

Dataset: Iris Dataset (Scikit-learn)

Evaluation Metric: Accuracy Score

The model is trained dynamically at runtime

🎯 Output

The app predicts one of the following Iris flower species:

Setosa

Versicolor

Virginica

📌 Note

Model persistence (.pkl file) is not used in this project as the model is trained at runtime, which is sufficient for learning and demonstration purposes.

👨‍💻 Author

Omesh Shewale

⭐ Acknowledgment

This project is completed as part of a learning-based internship task under CodeAlpha.
