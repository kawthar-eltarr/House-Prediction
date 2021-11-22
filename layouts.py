from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

layout1 = html.Div([
    html.H1('House Prediction Project'),
    dbc.Button(dcc.Link('Price Prediction Tool', href='/pred_tool')),
    dbc.Button(dcc.Link('Data Visualization Tool', href='/viz_tool'))
])

layout2 = html.Div(children=[
    html.H1('Price Prediction Tool'),
    dbc.Form(children=[
        dbc.Row(
            [
                dbc.Label("Longitude", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),
    
        dbc.Row(
                [
                    dbc.Label("Latitude", width="auto"),
                    dbc.Col(dbc.Input(), className="me-3", width="1")
                ],
                className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("House median age", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Total rooms", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),

        
        dbc.Row(
            [
                dbc.Label("Total bedrooms", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Population", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Number of households", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Median income", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Median house value", width="auto"),
                dbc.Col(dbc.Input(), className="me-3", width="1")               
            ],
            className="g-2"),
        
        html.Div(
            [
                dbc.Label("Dropdown", html_for="dropdown"),
                dcc.Dropdown(
                    id="dropdown",
                    options=[
                        {"label": "<1H OCEAN", "value": 0},
                        {"label": "INLAND", "value": 1},
                        {"label" : "NEAR OCEAN", "value": 4},
                        {"label" : "NEAR BAY", "value": 3},
                        {"label" : "ISLAND", "value": 2}
                        
                    ]),
            ],
            className="nav-item dropdown",
        ),
        
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(dbc.Button("Submit", color="primary"), width="auto"),
            ],
            className="g-2")
        ]),


])

layout3 = html.Div([
    html.H1('Data Visualization Tool'), 
])