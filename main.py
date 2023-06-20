import streamlit as st
import yfinance as yf
import pandas as pd

st.write(""" # Finance Dashboard """)
st.title("Stock Market App with *Streamlit*")
st.header("Data Science Web App")
st.sidebar.header("Nicholas Choi \n Extremely interested in Machine Learning and Data Science!")

# This is a function that captures the companies ticker

tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD', 'GOOG', 'NFLX')
dropdown = st.multiselect("Pick your assets", tickers)

start = st.date_input("Start", value=pd.to_datetime("2021-01-01"))
end = st.date_input("End", value=pd.to_datetime("today"))


def relativeret(df):
    rel = df.pct_change()
    cumret = (1 + rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


if len(dropdown) > 0:
    df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.header("Returns of {}".format(dropdown))
    st.line_chart(df)

