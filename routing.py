import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    dcc.Link('first', href='/first'),
    html.Br(),
    dcc.Link('second', href='/second'),

    html.Div(id='main')
])


graph_for_sla = dcc.Graph()
graph_for_priority = dcc.Graph()

@app.callback(
    Output(component_id="main", component_property="children"),
    [Input(component_id="url", component_property="pathname")]
)
def route(path):

    if path == "sla":
        return graph_for_sla


app.run_server(debug = True)
