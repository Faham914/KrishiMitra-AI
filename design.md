# KrishiMitra AI - System Design Document

## 1. System Overview

KrishiMitra AI is a Python-based agricultural price forecasting web application designed to help farmers and agricultural stakeholders make informed selling decisions.

The system provides 14-day price predictions for five major crops (Tomato, Onion, Potato, Rice, Wheat) across different mandis (markets). It also provides volatility-based risk assessment and SELL/HOLD recommendations.

The application is built entirely using Python and Streamlit, with CSV-based data storage and Prophet-based time-series forecasting.

---

## 2. High-Level Architecture

The system follows a simple monolithic architecture suitable for a hackathon-level prototype.

Flow:

User → Streamlit UI → Data Loader → Data Preprocessing → Prophet Model → Risk Engine → Recommendation Logic → Output Dashboard

There are no external APIs, databases, or distributed components.

---

## 3. Component Design

### 3.1 User Interface Layer (Streamlit)

- Commodity selection dropdown
- Market (mandi) selection dropdown
- Language selection (English, Hindi, Marathi)
- Forecast display (line chart)
- Risk level display
- SELL/HOLD recommendation display
- Commodity image rendering

Streamlit handles both UI rendering and backend execution in a single application.

---

### 3.2 Data Layer

- Historical mandi price data stored in CSV files
- Each commodity has its own dataset
- Pandas is used for:
  - Loading CSV files
  - Cleaning column names
  - Converting date formats
  - Preparing data for time-series forecasting

No external database system is used.

---

### 3.3 Forecasting Engine (Prophet)

- Facebook Prophet is used for time-series forecasting
- Input format: 
  - ds → date column
  - y → modal price
- Model learns:
  - Trend
  - Seasonality
- Generates 14-day future price predictions

Prophet was selected because:
- It handles seasonality well
- Works effectively on small-to-medium datasets
- Requires minimal hyperparameter tuning

---

### 3.4 Risk Engine

Risk is calculated using volatility of predicted prices.

Steps:
1. Extract 14-day predicted prices
2. Compute standard deviation using NumPy
3. Categorize risk:
   - Low
   - Medium
   - High

Thresholds are commodity-specific to reflect different volatility behaviors.

---

### 3.5 Recommendation Logic

SELL/HOLD decision is calculated as:

If Predicted Average Price > Current Price → HOLD  
Else → SELL

This provides a simple, interpretable decision support mechanism.

---

## 4. Data Flow

1. User selects commodity and market.
2. Corresponding CSV file is loaded.
3. Data is cleaned and formatted using Pandas.
4. Data is converted to Prophet-compatible format.
5. Prophet model is trained.
6. 14-day forecast is generated.
7. Volatility is calculated using NumPy.
8. Risk level is assigned.
9. Recommendation logic is applied.
10. Results and graph are displayed in Streamlit UI.

---

## 5. AI Model Explanation

Prophet is an additive time-series forecasting model.

It models time-series as:

Trend + Seasonality + Error

The model:
- Automatically detects trend changes
- Handles seasonality patterns
- Generates future predictions based on historical behavior

The model does not use deep learning or neural networks. It is optimized for interpretability and fast execution in small-scale forecasting tasks.

---

## 6. Deployment Design

- Source code hosted on GitHub.
- Application deployed using Streamlit Community Cloud.
- No external backend servers.
- No database services.
- No microservices architecture.

This lightweight deployment approach ensures simplicity and cost efficiency.

---

## 7. Limitations

- No real-time market data integration
- No weather or external factor integration
- Forecast accuracy depends on quality of historical data
- No user authentication system
- Limited to 5 commodities

---

## 8. Scalability & Future Improvements

- Add additional commodities
- Integrate government mandi APIs
- Add weather-based features
- Compare Prophet with other forecasting models
- Add SMS-based alerts
- Expand language support

The modular structure allows extension without major architectural changes.
