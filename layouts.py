from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from sklearn.preprocessing import StandardScaler

layout1 = html.Div([
    html.H1('House Prediction Project'),
    dbc.Button(dcc.Link('Price Prediction Tool', href='/pred_tool')),
    dbc.Button(dcc.Link('Data Visualization Tool', href='/viz_tool'))
])

layout2 = html.Div([
    html.H1('House Prediction Project'),
    dbc.Button(dcc.Link('Prediction with Machine Learning', href='/pred_tool/ml')),
    dbc.Button(dcc.Link('Prediction with Deep Learning', href='/pred_tool/dl'))
])

layout3 = html.Div(children=[
    html.H1('Price Prediction Tool with Machine Learning'),
    dbc.Form(children=[
        dbc.Row(
            [
                dbc.Label("Longitude", width="auto"),
                dbc.Col(dbc.Input(id='input-form-longitude', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),
    
        dbc.Row(
                [
                    dbc.Label("Latitude", width="auto"),
                    dbc.Col(dbc.Input(id='input-form-latitude', type='text'), className="me-3", width="1")
                ],
                className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("House median age", width="auto"),
                dbc.Col(dbc.Input(id='input-form-median-age', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Total rooms", width="auto"),
                dbc.Col(dbc.Input(id='input-form-rooms', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),

        
        dbc.Row(
            [
                dbc.Label("Total bedrooms", width="auto"),
                dbc.Col(dbc.Input(id='input-form-bedrooms', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Population", width="auto"),
                dbc.Col(dbc.Input(id='input-form-population', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Number of households", width="auto"),
                dbc.Col(dbc.Input(id='input-form-households', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Median income", width="auto"),
                dbc.Col(dbc.Input(id='input-form-income', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),
        
        dbc.Row(
            [
                dbc.Label("Median house value", width="auto"),
                dbc.Col(dbc.Input(id='input-form-house-value', type='text'), className="me-3", width="1")               
            ],
            className="g-2"),
        
        html.Div(
            [
                dbc.Label("Dropdown", html_for="dropdown"),
                dcc.Dropdown(
                    id="input-form-proximity",
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
        dbc.Button("Submit", color="primary", id='submit-val', n_clicks=0),

        html.Br(),
        
        html.Div(children=[
            html.H5('The machine learning model has predicted this value : '),
            html.H5(id='output-prediction', className="my-4", style={"font-weight": "bold"})]),
        ]),


])

layout4 = html.Div(children=[
    html.H1('Price Prediction Tool with Deep Learning'),
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

layout5 = html.Div([
    html.H1('Data Visualization Tool'), 
])



