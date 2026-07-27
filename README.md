📈 Market Volatility Monitor
A lightweight, interactive web application built with Python and Streamlit that tracks specific Indian and US stock market indices and highlights significant daily price movements.
Rather than manually checking multiple charts, this dashboard fetches live market data and instantly flags any asset in your portfolio that has moved by 2.5% or more compared to the previous day's closing price.
🌟 Key Features
 Live Market Data: Fetches real-time and historical pricing data using the Yahoo Finance API (⁠yfinance⁠).
 Automated Alerting Logic: Calculates percentage changes on demand and visually flags high-volatility assets with a 🚨 alert status.
 Cross-Market Tracking: Monitors a custom blend of 9 assets across different exchanges, including Nifty 50, S&P 500, Nasdaq, and Gold ETFs.
 Interactive GUI: Replaces terminal scripts with a clean, user-friendly Streamlit web interface containing easily readable data tables.
 Cloud Hosted: Fully deployed on Streamlit Community Cloud for 24/7 access from any device via a public URL.
🛠️ Tech Stack
 Python 3.10+ (Core logic)
 Streamlit (Web framework and UI)
 yfinance (Financial data retrieval)
 Pandas (Data table structuring and manipulation)
🚀 How to Use
Simply open the web app URL and click the "Check Market Now" button. The app will pull the latest data for all configured tickers, calculate the daily movement, and display a summary table, highlighting any assets that cross the 2.5% volatility threshold.
