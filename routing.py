import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    dcc.Link('first', href='/first'),
    dcc.Link('second', href='/second'),

    html.H1(id='main')
])

@app.callback(
    Output(component_id="main", component_property="children"),
    [Input(component_id="url", component_property="pathname")]
)
def route(path):
    return "{} path is selected!".format(path)


app.run_server(debug = True)
