# 🎯 JoSAA 2025 Branch Predictor

A data-driven Python application designed to help engineering aspirants predict their prospective seat allotments across various National Institutes of Technology (NITs) based on their JEE Main ranks. 

---

## 🛠️ Tech Stack & Architecture

*   **Logic & Processing:** Python, Pandas (for dataset parsing)
*   **Dataset:** Official 2025 JoSAA opening and closing rank data
*   **Interface:** Command Line

---

## 🚀 How to Run Locally

To run this predictor on your own machine, execute these commands in your terminal:

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the directory:
   ```bash
   cd JoSAA-predictor
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

---

## 🧠 Logic & Core Functionality

1. **Data Ingestion:** The script reads raw CSV/Excel datasets containing previous years' JoSAA seat allotment trends.
2. **Filtering Engine:** Takes user inputs such as JEE Main Rank, Quota (Home State vs. Other State), and Gender Pool.
3. **Cutoff Matching:** Iterates through the records to find branches where the user's rank falls safely within the historical opening and closing range, outputting a list of viable college options.
