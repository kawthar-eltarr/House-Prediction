from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

# Prep for layout 5 (dataviz)
# Getting data
df = pd.read_csv('housing.csv')
map_data = df[['longitude', 'latitude', 'median_house_value', 'ocean_proximity', 'population', 'total_rooms', 'total_bedrooms',
     'households']]

max_house_value, min_house_value = map_data.median_house_value.max(), map_data.median_house_value.min()

max_pop, min_pop, std_pop = map_data.population.max(), map_data.population.min(), map_data.population.std()
mean_pop = map_data.population.mean()

mean_long, mean_lat = map_data.latitude.mean(), map_data.longitude.mean()

map_data.loc[:, 'mean_rooms'] = (map_data.total_rooms / map_data.households)

max_mean_rooms, min_mean_rooms = map_data.mean_rooms.max(), map_data.mean_rooms.min()

map_data.loc[:,'mean_bedrooms'] = map_data.total_bedrooms / map_data.households
max_mean_bedrooms, min_mean_bedrooms = map_data.mean_bedrooms.max(), map_data.mean_bedrooms.min()


def mark_list(var1, var2, k=5, r=2):
    """Returns a list to be used as marker generator"""
    if r == 0:
        return [round(var1 + i * (var2 - var1) / k) for i in range(k)]
    return [round(var1 + i * (var2 - var1) / k, r) for i in range(k)]


layout1 = html.Div(
    className="card border-secondary mb-3",
    children=[
        html.H1('House Prediction Project', style={'margin': 'inherit'}),
        dbc.Button(dcc.Link('Price Prediction Tool', href='/pred_tool'), className="btn btn-primary btn-lg",
                   style={'margin': 'auto'}),
        html.Br(),
        dbc.Button(dcc.Link('Data Visualization Tool', href='/viz_tool'), className="btn btn-primary btn-lg",
                   style={'margin': 'auto'}),
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
        dbc.Button(dcc.Link('Prediction with Machine Learning', href='/pred_tool/ml'),
                   className="btn btn-primary btn-lg", style={'margin': 'auto'}),
        html.Br(),
        dbc.Button(dcc.Link('Prediction with Deep Learning', href='/pred_tool/dl'), className="btn btn-primary btn-lg",
                   style={'margin': 'auto'}),
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
    dbc.Form(style={'margin-left': '2%', 'margin-right': '2%'}, children=[
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
                        {"label": "NEAR OCEAN", "value": 4},
                        {"label": "NEAR BAY", "value": 3},
                        {"label": "ISLAND", "value": 2}

                    ], style={'color': 'pink'}),
            ],
            className="nav-item dropdown",
        ),
        html.Br(),

        dbc.Button("Submit", color="primary", id='submit-val-ml', n_clicks=0),

        html.Br(),

        html.Div(children=[
            html.H5('The machine learning model has predicted this value : '),
            html.H5(id='output-prediction-ml', className="my-4", style={"font-weight": "bold"})]),
    ]),

],
    style={
        'margin': 'auto',
        'max-width': '95vw',
        'margin-top': '3%',
        'textAlign': 'center'
        })

layout4 = html.Div(className="card border-secondary mb-3", children=[
    html.H1('Price Prediction Tool with Deep Learning', style={'margin': 'inherit'}),
    dbc.Form(style={'margin-left': '2%', 'margin-right': '2%'}, children=[
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
                    id="input-form-proximity", style={'color': 'pink'},
                    options=[
                        {"label": "<1H OCEAN", "value": 0},
                        {"label": "INLAND", "value": 1},
                        {"label": "NEAR OCEAN", "value": 4},
                        {"label": "NEAR BAY", "value": 3},
                        {"label": "ISLAND", "value": 2}

                    ]),
            ],
            className="nav-item dropdown",
        ),

        html.Br(),

        dbc.Button("Submit", color="primary", id='submit-val-dl', n_clicks=0),
        
        html.Br(),
        html.Div(children=[
            html.H5('The deep learning model has predicted this value : '),
            html.H5(id='output-prediction-dl', className="my-4", style={"font-weight": "bold"})])
    ]),

], style={
        'margin': 'auto',
        'max-width': '95vw',
        'margin-top': '3%',
        'textAlign': 'center'
        })

layout5 = html.Div(children=[
    html.Div([
        html.H1(children='Housing prices in California'),

        html.H4(id='mean_price', style={'text-decoration': 'underline'}),

        html.Div(
            html.Div(
                html.P(
                    [
                        html.H4('Type of graph'),
                        dcc.Dropdown(
                            id='dropdown_graph', style={'color': 'pink'},
                            options=[
                                {'label': 'Map', 'value': 'map'},
                                {'label': 'Histogram', 'value': 'hist'}
                            ],
                            value='hist'
                        ),

                        html.H4(children='Price', className="card-title",
                                style={'marginTop': 10}),
                        dcc.RangeSlider(
                            id='price_range',
                            marks={str(x): str(x) for x in mark_list(min_house_value, max_house_value)},
                            tooltip={"placement": "top", "always_visible": True},
                            min=min_house_value,
                            max=max_house_value,
                            step=round((max_house_value - min_house_value) / 30, 2),
                            pushable=1,
                            value=[min_house_value + (2 * (max_house_value - min_house_value) / 30),
                                   max_house_value - (2 * (max_house_value - min_house_value) / 30)]
                        ),

                        html.H4(children='Population', className="card-title"),
                        dcc.RangeSlider(
                            id='population_range',
                            marks={str(x): str(x) for x in mark_list(min_pop, mean_pop)},
                            tooltip={"placement": "top", "always_visible": True},
                            min=min_pop,
                            max=mean_pop,
                            step=round((mean_pop - min_pop) / 30, 2),
                            pushable=1,
                            value=[min_pop + (2 * (mean_pop - min_pop) / 30),
                                   mean_pop - (2 * (mean_pop - min_pop) / 30)]
                        ),

                        # to be exponential
                        html.H4(children='Mean rooms per households', className="card-title"),
                        dcc.RangeSlider(
                            id='mean_rooms',
                            marks={str(x): str(x) for x in mark_list(min_mean_rooms, max_mean_rooms, r=0)},
                            tooltip={"placement": "top", "always_visible": True},
                            min=min_mean_rooms,
                            max=max_mean_rooms,
                            step=round((max_mean_rooms - min_mean_rooms) / 80, 2),
                            pushable=1,
                            value=[min_mean_rooms, max_mean_rooms - (50 * (max_mean_rooms - min_mean_rooms) / 80)]
                        ),

                        # to be exponential
                        html.H4(children='Mean bedrooms per households', className="card-title"),
                        dcc.RangeSlider(
                            id='mean_bedrooms',
                            marks={str(x): str(x) for x in mark_list(min_mean_bedrooms, max_mean_bedrooms, r=0)},
                            tooltip={"placement": "top", "always_visible": True},
                            min=min_mean_bedrooms,
                            max=max_mean_bedrooms,
                            step=round((max_mean_bedrooms - min_mean_bedrooms) / 80, 2),
                            pushable=1,
                            value=[min_mean_bedrooms,
                                   max_mean_bedrooms - (50 * (max_mean_bedrooms - min_mean_bedrooms) / 80)]
                        ),

                        dcc.RadioItems(
                            id='loc_choice',
                            options=[
                                {'label': 'Near Ocean', 'value': 'NEAR OCEAN'},
                                {'label': '<1h from Ocean', 'value': '<1H OCEAN'},
                                {'label': 'Inland', 'value': 'INLAND'},
                                {'label': 'Near San Francisco Bay', 'value': 'NEAR BAY'},
                                {'label': 'Island', 'value': 'ISLAND'},
                                {'label': 'Whatever', 'value': 'WTVR'}
                            ],
                            value='<1H OCEAN'
                        )],
                    className='card_text'
                ),
                className='card-body'
            ),
            className="card border-secondary mb-3", style={'max-width': '30rem', 'marginLeft': 750, 'marginTop': 50}
        ),
    ], style={'marginBottom': 50, 'marginTop': 50, 'marginLeft': 50, 'marginRight': 25}),

    html.Div(
        dcc.Graph(
            id='myMap'
        ),
        style={'position': 'relative', 'bottom': 700, 'left': 50, 'width': 700}
    )
])
