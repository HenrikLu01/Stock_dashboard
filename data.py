import yfinance as yf
import streamlit as st

@st.cache_data
def load_ticker_data(symbol):
    ticker = yf.Ticker(symbol)
    return {
        "dividendYield": ticker.info.get("dividendYield"),
        "forwardPE": ticker.info.get("forwardPE"),
        "history": ticker.history(period="6mo").reset_index(),
        "netIncome": ticker.get_income_stmt(as_dict=True, freq='quarterly'),
        #"balanceSheet": ticker.get_balance_sheet(as_dict=True, freq='quarterly')
    }