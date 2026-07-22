import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")


def build_figure(region):
    if region == "all":
        filtered = df
    else:
        filtered = df[df["Region"] == region]

    daily_sales = filtered.groupby("Date", as_index=False)["Sales"].sum()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        labels={"Date": "Date", "Sales": "Sales ($)"},
    )
    fig.update_traces(line_color="#e83e8c", line_width=3)
    fig.update_layout(
        plot_bgcolor="#fff9fb",
        paper_bgcolor="#fff9fb",
        font_family="Verdana, sans-serif",
        title=dict(
            text=f"Pink Morsel Sales - {region.capitalize()}",
            font=dict(size=20, color="#7a1f4d"),
        ),
        margin=dict(t=60, l=40, r=20, b=40),
    )
    return fig


app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#ffeef5",
        "fontFamily": "Verdana, sans-serif",
        "padding": "40px",
        "minHeight": "100vh",
    },
    children=[
        html.H1(
            "Soul Foods: Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#7a1f4d", "marginBottom": "10px"},
        ),
        html.P(
            "Filter sales by region to explore the impact of the January 2021 price increase.",
            style={"textAlign": "center", "color": "#a15277", "marginBottom": "30px"},
        ),
        html.Div(
            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                    {"label": "All", "value": "all"},
                ],
                value="all",
                inline=True,
                labelStyle={"marginRight": "20px", "fontSize": "16px", "color": "#7a1f4d"},
                inputStyle={"marginRight": "6px"},
            ),
            style={"textAlign": "center", "marginBottom": "30px"},
        ),
        html.Div(
            dcc.Graph(id="sales-line-chart"),
            style={
                "backgroundColor": "#ffffff",
                "borderRadius": "12px",
                "padding": "20px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                "maxWidth": "1000px",
                "margin": "0 auto",
            },
        ),
    ],
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    return build_figure(selected_region)


if __name__ == "__main__":
    app.run(debug=True)
