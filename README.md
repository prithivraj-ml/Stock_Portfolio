# 📈 Stock Market Visualization

This project provides an **interactive stock analysis and visualization tool** built with Python.  
It allows users to fetch historical stock prices, analyze trends, and visualize stock performance over custom date ranges.

---

## 📄 Overview
The main objective of this project is to:
- Fetch **real-time and historical stock data** using `yfinance`
- Visualize stock price movements using **line graphs**
- Allow users to **select date ranges** and view stock performance
- Build an interactive web-based visualization with **Flask**

This tool is helpful for investors, analysts, and learners to understand market behavior and explore stock movements visually.

---

## 📊 Features
1. **Stock Data Fetching** – Retrieve stock data (2022–2023 or custom ranges) using `yfinance`  
2. **Interactive Visualization** – Line graphs to analyze stock price fluctuations  
3. **Multiple Stocks Support** – Select different tickers for analysis  
4. **Technical Indicators** (with `TA-Lib`) – (optional) Add advanced analytics like moving averages, RSI, MACD  
5. **Web Dashboard** – Simple Flask interface for easy interaction  

---

## ⚙️ Technologies Used
- **Python**
- **Flask** (Web framework for dashboard)
- **yfinance** (Fetch historical stock market data)
- **Matplotlib** (Data visualization)
- **TA-Lib** (Technical indicators – moving averages, RSI, MACD)
- **Pandas & NumPy** (Data analysis & manipulation)

---

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/prithivraj-ml/Stock_Portfolio.git
   cd Stock_Portfolio
   
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Run the application:

   ```bash
   python app.py
   
4. Open your browser and go to:

   ```cpp
   http://127.0.0.1:5000/

🌟 Future Enhancements
- Add candlestick charts for better financial insights

- Compare multiple stocks in one graph

- Integrate real-time live stock updates

- Provide export options (CSV, Excel, or PDF reports)

- Extend to portfolio analysis & performance tracking

👤 Author
Prithivraj

GitHub: prithivraj-ml

Passionate about AI/ML & Data Visualization
