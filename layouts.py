from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


layout1 = html.Div(
    className="card border-secondary mb-3", 
    children=[
    html.H1('House Prediction Project', style={'margin': 'inherit'}),
    dbc.Button(dcc.Link('Price Prediction Tool', href='/pred_tool'), className="btn btn-primary btn-lg", style={'margin': 'auto'}),
    html.Br(),
    dbc.Button(dcc.Link('Data Visualization Tool', href='/viz_tool'), className="btn btn-primary btn-lg", style={'margin': 'auto'}),
    html.H1(style={'margin-top': '2%'})],
    style={
        'margin': 'auto', 
        'max-width': '95vw', 
        'margin-top': '3%',
        'textAlign': 'center',
        }
    )

layout2 = html.Div(
    className="card border-secondary mb-3", 
    children=[
    html.H1('House Prediction Project', style={'margin': 'inherit'}),
    dbc.Button(dcc.Link('Prediction with Machine Learning', href='/pred_tool/ml'), className="btn btn-primary btn-lg", style={'margin': 'auto'}),
    html.Br(),
    dbc.Button(dcc.Link('Prediction with Deep Learning', href='/pred_tool/dl'), className="btn btn-primary btn-lg", style={'margin': 'auto'}),
    html.H1(style={'margin-top': '2%'})],
    style={
        'margin': 'auto', 
        'max-width': '95vw', 
        'margin-top': '3%',
        'textAlign': 'center',
        }
    )

layout3 = html.Div(className="card border-secondary mb-3", children=[
    html.H1('Price Prediction Tool with Machine Learning', style={'margin-top': '1.5%'}),
    dbc.Form(style = {'margin-left': '2%', 'margin-right': '2%'}, children=[
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
                        
                    ], style={'color':'pink'}),
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
    
    ], 
    
    style={
        'margin': 'auto', 
        'max-width': '95vw', 
        'margin-top': '3%',
        'textAlign': 'center',
        })

layout4 = html.Div(children=[
    html.H1('Price Prediction Tool with Deep Learning', style={'margin': 'inherit'}),
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
            className="g-2"),
        html.Br()
        ]),


])

layout5 = html.Div([
    html.H1('Data Visualization Tool'), 
])



