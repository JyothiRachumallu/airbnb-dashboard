# 🏠 Airbnb Analytics Dashboard (Production-Ready)

## 📌 Overview

An end-to-end data analytics dashboard built using **Streamlit**, **PostgreSQL**, and **SQLAlchemy**.
This project demonstrates real-world data engineering and analytics workflow including data cleaning, database integration, and interactive visualization.

---

## ⚙️ Tech Stack

* Python
* Streamlit
* PostgreSQL
* SQLAlchemy
* Pandas
* Plotly
* Docker

---

## 🧩 Project Architecture

CSV Data → Data Cleaning → PostgreSQL Database → Streamlit Dashboard

---

## 🛠️ Setup Instructions

### 1️⃣ Create PostgreSQL Database

```sql
CREATE DATABASE airbnb_db;
```

---

### 2️⃣ Configure Environment Variables

Create a `.env` file:

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=airbnb_db
```

---

### 3️⃣ Run Data Pipeline

```bash
python data_pipeline.py
```

---

### 4️⃣ Run Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 📊 Features

* Data Cleaning & Preprocessing
* PostgreSQL Database Integration
* Interactive Streamlit Dashboard
* Geo Analysis (Map + Heatmap)
* Filters & KPI Metrics
* SQL-Based Aggregations
* Downloadable Dataset

---

## 🐳 Docker Support

### Build Image

```bash
docker build -t airbnb-dashboard .
```

### Run Container

```bash
docker run -p 8501:8501 --env-file .env airbnb-dashboard
```

---

## 📁 Project Structure

```
├── streamlit_app.py
├── data_pipeline.py
├── database.py
├── models.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env.example
├── Airbnb_Open_Data.csv
└── README.md
```

---

## 🚀 Future Improvements

* Machine Learning Price Prediction
* FastAPI Backend Integration
* Cloud Deployment (AWS / Render / Streamlit Cloud)

---

## 💡 Key Highlights

* Built an end-to-end analytics pipeline
* Implemented database-driven dashboard
* Applied real-world data cleaning techniques
* Designed production-ready Docker setup

---

## 👨‍💻 Author

**Jyothi Rachumallu**
Associate Software Engineer | Python Developer

---

## ⭐ If you like this project

Give it a star ⭐
