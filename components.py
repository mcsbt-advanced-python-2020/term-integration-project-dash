import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("firemen.csv")

districts = list(df["DISTRITO"].unique())
months = list(df["MES"].unique())
years = list(df["AÑO"].unique())


app.layout = html.Div(children=[
    html.H1("Fires by district and month"),

    html.H2("Pick a district"),
    dcc.Dropdown(id="districts", options=[{"label": d, "value": d} for d in districts], multi=True, value=["CENTRO"]),

    html.H2("Select month range"),
    dcc.RangeSlider(id="months", marks= {k: v for k, v in enumerate(months)}, step=None, min=0, max=11, value=[0,2]),

    dcc.Graph(id="fires", figure={"data":[], "layout":{"title": "fires"}})
])


@app.callback(
    Output(component_id="fires", component_property="figure"),
    [
        Input(component_id="districts", component_property="value"),
        Input(component_id="months", component_property="value")
    ]
)
def update_fires_graph(districts, months_selected):

    current_months = [months[n] for n in range(months_selected[0], months_selected[1] + 1)]

    filtered = df[df["DISTRITO"].isin(districts) & df["MES"].isin(current_months)]

    print(filtered)

    data = []

    for district in filtered["DISTRITO"].unique():
        count = filtered[filtered["DISTRITO"] == district]["TOTAL"].sum()
        row = {'x': filtered["DISTRITO"].unique(), 'y': [count], 'type': 'bar', 'name': district}
        data.append(row)

    fig={
      "data": data,
      "layout": {
        "title": "fires"
      }
    }

    return fig


app.run_server(debug=True)
