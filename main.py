import numpy as np
from utils import load_and_clean_data
from model import train_model, make_forecast

DATA_PATH = r"F:\krishimitra_ai\data\mandi_data.csv"

df = load_and_clean_data(
    DATA_PATH,
    commodity_name="Tomato",
    market_name="Nagpur"
)

model = train_model(df)
forecast = make_forecast(model, periods=7)

current_price = df["y"].iloc[-1]
future_prices = forecast["yhat"].tail(7)
predicted_avg = future_prices.mean()

decision = "HOLD" if predicted_avg > current_price else "SELL"

# Volatility calculation
volatility = np.std(future_prices)

if volatility > 300:
    risk = "High"
elif volatility > 150:
    risk = "Medium"
else:
    risk = "Low"


print("\n========== KrishiMitra AI Output ==========")
print("Current Price:", current_price)
print("Predicted Avg (Next 7 Days):", round(predicted_avg, 2))
print("Recommendation:", decision)
print("Risk Level:", risk)
print("===========================================")
