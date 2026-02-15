# ============================================
# KrishiMitra AI - Cloud Ready Version
# Developed by: Mohammad Faham Khan, K.N. Gautam
# ============================================

import streamlit as st
import numpy as np
import pandas as pd
from utils import load_and_clean_data
from model import train_model, make_forecast
import os

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="KrishiMitra AI", layout="wide")

# ------------------------------------------------
# Developer Credits
# ------------------------------------------------
st.markdown("### 👨‍💻 Developers")
st.markdown("- Mohammad Faham Khan")
st.markdown("- K.N. Gautam")

# ------------------------------------------------
# Language Translations
# ------------------------------------------------
translations = {
    "English": {
        "title": "🌾 KrishiMitra AI",
        "subtitle": "Predictive Crop Price & Decision Intelligence System",
        "select_commodity": "Select Commodity",
        "select_market": "Select Market",
        "predict": "Predict Price",
        "current_price": "Current Price",
        "predicted_avg": "Predicted Avg (Next 14 Days)",
        "recommendation": "Recommendation",
        "risk": "Risk Level",
        "forecast": "Price Forecast"
    },
    "Hindi": {
        "title": "🌾 कृषिमित्र एआई",
        "subtitle": "फसल मूल्य पूर्वानुमान प्रणाली",
        "select_commodity": "फसल चुनें",
        "select_market": "मंडी चुनें",
        "predict": "मूल्य पूर्वानुमान देखें",
        "current_price": "वर्तमान मूल्य",
        "predicted_avg": "अगले 14 दिनों का अनुमानित औसत मूल्य",
        "recommendation": "सुझाव",
        "risk": "जोखिम स्तर",
        "forecast": "मूल्य पूर्वानुमान"
    },
    "Marathi": {
        "title": "🌾 कृषिमित्र एआय",
        "subtitle": "पीक किंमत अंदाज प्रणाली",
        "select_commodity": "पीक निवडा",
        "select_market": "बाजार निवडा",
        "predict": "किंमत अंदाज पहा",
        "current_price": "सध्याची किंमत",
        "predicted_avg": "पुढील 14 दिवसांची अंदाजित सरासरी किंमत",
        "recommendation": "शिफारस",
        "risk": "जोखीम पातळी",
        "forecast": "किंमत अंदाज"
    },
    
    "Bengali": {
        "title": "🌾 কৃষিমিত্র এআই",
        "subtitle": "ফসল মূল্য পূর্বাভাস ব্যবস্থা",
        "select_commodity": "ফসল নির্বাচন করুন",
        "select_market": "বাজার নির্বাচন করুন",
        "predict": "মূল্য পূর্বাভাস দেখুন",
        "current_price": "বর্তমান মূল্য",
        "predicted_avg": "পরবর্তী ১৪ দিনের গড় পূর্বাভাস মূল্য",
        "recommendation": "পরামর্শ",
        "risk": "ঝুঁকি স্তর",
        "forecast": "মূল্য পূর্বাভাস"
    },
    "Tamil": {
        "title": "🌾 கிரிஷிமித்ரா AI",
        "subtitle": "பயிர் விலை முன்னறிவிப்பு அமைப்பு",
        "select_commodity": "பயிரைத் தேர்ந்தெடுக்கவும்",
        "select_market": "சந்தையைத் தேர்ந்தெடுக்கவும்",
        "predict": "விலை கணிக்க",
        "current_price": "தற்போதைய விலை",
        "predicted_avg": "அடுத்த 14 நாட்களின் சராசரி கணிப்பு",
        "recommendation": "பரிந்துரை",
        "risk": "ஆபத்து நிலை",
        "forecast": "விலை கணிப்பு"
    }
}

language = st.selectbox("Select Language / भाषा निवडा", list(translations.keys()))
t = translations[language]

st.title(t["title"])
st.caption("Empowering rural farmers with AI-driven market intelligence for sustainable decision-making.")
st.subheader(t["subtitle"])

# ------------------------------------------------
# Dataset Mapping (Relative Paths for Cloud)
# ------------------------------------------------
DATASETS = {
    "Tomato": "data/Tomato_mandi_data.csv",
    "Onion": "data/Onion_mandi_data.csv",
    "Potato": "data/Potato_mandi_data.csv",
    "Rice": "data/Rice_mandi_data.csv",
    "Wheat": "data/Wheat_mandi_data.csv"
}

commodity = st.selectbox(t["select_commodity"], list(DATASETS.keys()))

# Emoji Display
commodity_emojis = {
    "Tomato": "🍅",
    "Onion": "🧅",
    "Potato": "🥔",
    "Rice": "🌾",
    "Wheat": "🌾"
}

st.markdown(f"### {commodity_emojis.get(commodity, '')} {commodity}")

# Image Display (Relative Path)
image_path = f"images/{commodity}.jpg"
if commodity == "Potato":
    image_path = "images/Potatoes.jpg"

if os.path.exists(image_path):
    st.image(image_path, width=250)

DATA_PATH = DATASETS[commodity]

# Load Markets
temp_df = pd.read_csv(DATA_PATH)
temp_df.columns = temp_df.columns.str.strip()

markets = sorted(temp_df["Market"].unique())
market = st.selectbox(t["select_market"], markets)

# ------------------------------------------------
# Prediction Section
# ------------------------------------------------
if st.button(t["predict"]):

    with st.spinner("Training AI model and generating forecast..."):

        df = load_and_clean_data(DATA_PATH, commodity, market)

        if df.empty:
            st.error("No data available for selected commodity and market.")
        else:
            model = train_model(df)
            forecast = make_forecast(model, periods=14)

            current_price = df["y"].iloc[-1]
            future_prices = forecast["yhat"].tail(14)
            predicted_avg = future_prices.mean()

            decision = "HOLD" if predicted_avg > current_price else "SELL"

            volatility = np.std(future_prices)

            if volatility > 300:
                risk = "High"
            elif volatility > 150:
                risk = "Medium"
            else:
                risk = "Low"

            st.markdown("## 📊 Results")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**{t['current_price']}:** ₹ {current_price} per quintal")
                st.write(f"**{t['predicted_avg']}:** ₹ {round(predicted_avg, 2)} per quintal")

            with col2:
                st.write(f"**{t['recommendation']}:** {decision}")
                st.write(f"**{t['risk']}:** {risk}")

            st.markdown(f"### 📈 {t['forecast']}")
            chart_data = forecast[["ds", "yhat"]].set_index("ds")
            st.line_chart(chart_data)

            st.caption("Forecast generated using time-series AI model based on historical mandi data and volatility analysis.")
