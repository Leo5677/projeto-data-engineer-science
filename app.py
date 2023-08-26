from flask import *
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
from models.connection import databaseMongoDB
from forex_python.converter import CurrencyRates

# INTANCIAÇÃO DO APP
app = Flask(__name__, template_folder="./templates")

# ROTA HOME
@app.route("/", methods=["GET"])
def home():
    return render_template(
        "home.html",
        chart_five_years=lastFiveYearsChart(),
        chart_thirty_days=lastThirtyDaysChart()
    )

# GERA UM GRÁFICO COM O VALOR DO BTC DOS ÚLTIMOS 5 ANOS
def lastFiveYearsChart():
    # DATA DE HOJE E DE 5 ANOS ATRÁS
    date_now = datetime.now().strftime("%Y-%m-%d")
    date_five_years = (datetime.now() - timedelta(days=5 * 365)).strftime("%Y-%m-%d")

    # API - BITCOIN
    url = f"https://coincodex.com/api/coincodex/get_coin_history/BTC/{date_five_years}/{date_now}/1"
    response = requests.get(url)
  
    # CONVERTE OS DADOS PARA O FORMATO CORRETO
    documents = [
        {
            "timestamp": data[0],
            "price": data[1],
            "volume": data[2],
            "volume_2": data[3]
        }
        for data in response.json()["BTC"]
    ]

    # MONGODB - INSERE DADOS APENAS SE NÃO EXISTIREM
    collection = databaseMongoDB()["last_five_years"]

    for document in documents:
        filter = {"timestamp": document["timestamp"]}
        collection.update_one(filter, {"$set": document}, upsert=True)

    # CONVERTE DÓLAR PARA REAL
    dolar_real = CurrencyRates().get_rate("USD", "BRL")

    # MONGODB - RECUPERA OS REGISTROS E CRIA A LISTA DE DATA E DE VALORES
    date_list = [pd.to_datetime(entry["timestamp"], unit="s") for entry in collection.find({})]
    values_list = [entry["price"] * dolar_real for entry in collection.find({})]

    # REALIZA A INSTANCIAÇÃO DO PANDAS COM OS DADOS
    df = pd.DataFrame({
        'Data': date_list,
        'Valor': values_list
    })

    # REALIZA A INSTANCIAÇÃO DO GRÁFICO E PERSONALIZA O LAYOUT
    chart = go.Figure([go.Scatter(x=df['Data'], y=df['Valor'], mode='lines')])
    chart.update_layout(
        title="Histórico do Valor do Bitcoin - Últimos 5 Anos",
        xaxis_title='Ano',
        yaxis_title='Valor',
        showlegend=False,
        height=600,
        width=1200
    )

    return chart.to_html(full_html=False)

# GERA UM GRÁFICO COM O VALOR DO BTC DOS ÚLTIMOS 30 DIAS
def lastThirtyDaysChart():
    # DATA DE HOJE / 30 DIAS ATRÁS
    date_thirty_days = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    
    # API - BITCOIN
    url = f"https://rest.coinapi.io/v1/ohlcv/KRAKENFTS_PERP_BTC_USD/history?period_id=1DAY&time_start={date_thirty_days}"
    headers = {"X-CoinAPI-Key": "AF522BD8-5A06-409A-9AC9-FAABE8C7FA1D"}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # MONGODB - INSERE DADOS APENAS SE NÃO EXISTEREM
    collection = databaseMongoDB()["last_thirty_days"]
    
    for document in data:
        filter = {"time_period_start": document["time_period_start"]}
        collection.update_one(filter, {"$set": document}, upsert=True)
    
    # CONVERTE DÓLAR PARA REAL
    dolar_real = CurrencyRates().get_rate("USD", "BRL")

    # MONGODB - RECUPERA OS REGISTROS E CRIA AS LISTAS PARA O CANDLESTICK
    time_period_start = [entry["time_period_start"] for entry in collection.find({})]
    price_open = [entry["price_open"] * dolar_real for entry in collection.find({})]
    price_high = [entry["price_high"] * dolar_real for entry in collection.find({})]
    price_low = [entry["price_low"] * dolar_real for entry in collection.find({})]
    price_close = [entry["price_close"] * dolar_real for entry in collection.find({})]

    # REALIZA A INSTANCIAÇÃO DO GRÁFICO E PERSONALIZA O LAYOUT
    chart = go.Figure(data=[go.Candlestick(
        x=time_period_start,
        open=price_open,
        high=price_high,
        low=price_low,
        close=price_close
    )])
    chart.update_layout(
        title='Histórico do Valor do Bitcoin - Últimos 30 Dias',
        xaxis_title='Período',
        yaxis_title='Valor',
        height=600,
        width=1200
    )

    return chart.to_html(full_html=False)


if __name__ == '__main__':
    app.run()
