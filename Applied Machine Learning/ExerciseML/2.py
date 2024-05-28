from sklearn.linear_model import LinearRegression
import numpy as np
news_sentiment = np.array([0.2, 0.5, 0.3, -0.1, 0.4, 0.6, 0.1, -0.2, 0.3, 0.0]).reshape(-1,1)
stock_price = [50, 55, 48, 45, 52, 58, 53, 47, 51, 50]
model = LinearRegression()
model.fit(news_sentiment,stock_price)
print(f"Intercept: {model.intercept_}, Coefficients: {model.coef_}")

