# 🚢 Titanic Data Analysis Project

## 📌 Overview
This project performs data analysis on the famous Titanic dataset using Python and Pandas.  
It includes data cleaning, exploratory data analysis (EDA), grouping, filtering, and insights extraction.

---

## 📊 Dataset
The dataset used is the **Titanic dataset (train.csv)**, which contains information about passengers such as:
- Passenger class
- Age
- Gender
- Fare
- Survival status

---

## 🛠 Tools & Libraries
- Python 🐍
- Pandas 📊

---


---

## 🔍 Data Exploration
The dataset was explored using:
- `.head()` → view first rows
- `.info()` → check data types & missing values
- `.describe()` → statistical summary

---

## 🧹 Data Cleaning
The following cleaning steps were performed:
- Filled missing values in **Age** using median
- Filled missing values in **Embarked** using mode
- Removed duplicate rows
- Verified and handled missing data

---

## 📈 Data Analysis

### 🔹 Survival Rate by Gender
- Females had a significantly higher survival rate than males.

### 🔹 Survival Rate by Class
- 1st class passengers had the highest survival rate
- 3rd class passengers had the lowest survival rate

### 🔹 Average Age per Class
- Calculated using groupby on passenger class

### 🔹 Survival Rate by Age Group
Age groups were created:
- Child (0–12)
- Teen (13–18)
- Adult (19–60)
- Senior (60+)

Children had higher survival rates compared to adults.

---

## 🔎 Filtering Analysis

The dataset was filtered to find:
- Female passengers who survived
- Children who survived
- 1st class passengers with high survival probability

---

## 💡 Key Insights

- 👩 **Females were more likely to survive** than males.
- 🎟 **Passenger class strongly affected survival chances**.
- 🧒 **Children were given priority during evacuation**.
- ⭐ The highest survival group was:
  > Female passengers in 1st class, especially younger individuals.

---

## 🚀 How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/titanic-project.git
