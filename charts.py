import altair as alt
import pandas as pd

def history_chart(ticker_data):
    data = ticker_data["history"]
    min_price = data["Close"].min()
    max_price = data["Close"].max()
    margin = 0.01 * (max_price - min_price) #Sets border margin
    # Example scaling rule (tune as needed)
    price_df = pd.DataFrame({
        "date": data["Date"],
        "price": data["Close"]
    })
    price_chart = alt.Chart(price_df).mark_line().encode(
        x="date:T",
        y=alt.Y(
            "price:Q",
            scale=alt.Scale(domain=[min_price - margin,
                                    max_price + margin])
        )
    ).properties(height=300)
    return price_chart

def quarterly_chart(ticker_data):
    net_income_dict = {}
    data = ticker_data["netIncome"]
    for date,data in data.items():
        quarter = f"{date.year}-Q{date.quarter}"

        net_income_dict[quarter] = data["NetIncomeCommonStockholders"]
    fcf_df = pd.DataFrame(
        list(net_income_dict.items()),
        columns=["quarter", "value"]
    )
    fcf_chart = alt.Chart(fcf_df).mark_bar(size=30).encode(
        x="quarter:N",
        y="value:Q"
    )
    return fcf_chart
