from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

layout1 = html.Div([
    html.H1('House Prediction Project'),
    dbc.Button(dcc.Link('Price Prediction Tool', href='/pred_tool')),
    dbc.Button(dcc.Link('Data Visualization Tool', href='/viz_tool'))
])

layout2 = html.Div([
    html.H1('Price Prediction Tool'),
])

layout3 = html.Div([
    html.H1('Data Visualization Tool'), 
])