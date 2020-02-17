import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask, render_template
import pandas as pd


server = Flask(__name__)

@server.route('/')
def index():
    return render_template("index.html")

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div(children=[
    html.H1("This is from the dash app"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
