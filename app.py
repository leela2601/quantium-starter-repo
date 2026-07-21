import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Sales ($)"},
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Visualiser"),
    dcc.Graph(id="sales-line-chart", figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)
