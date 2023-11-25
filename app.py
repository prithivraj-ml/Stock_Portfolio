from flask import Flask, render_template, request
import yfinance as yf
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)
    return stock

# Function to plot line graph
def plot_line_graph(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.title('Stock Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    # Convert plot to base64 image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url

# Render homepage with stock data and graph
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        stock_data = fetch_stock_data(ticker, start_date, end_date)
        graph = plot_line_graph(stock_data)

        return render_template('index.html', graph=graph)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
