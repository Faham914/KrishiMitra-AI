from prophet import Prophet

def train_model(df):
    model = Prophet()
    model.fit(df)
    return model

def make_forecast(model, periods=7):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
