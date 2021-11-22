# Dash
from dash import Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
# Plotly
import plotly.graph_objects as go
import plotly.express as px
# Data Manipulation
import pandas as pd
import numpy as np

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('housing.csv')
map_data = df[['longitude', 'latitude', 'median_house_value', 'ocean_proximity', 'population']]

# Taking random data to test the map
rnd = np.random.randint(0, df.shape[0], 5000)
map_data = map_data.iloc[rnd, :]

#### Layout

max_house_value, min_house_value = map_data.median_house_value.max(), map_data.median_house_value.min()
max_pop, min_pop, std_pop = map_data.population.max(), map_data.population.min(), map_data.population.std()
mean_pop = map_data.population.mean()
mean_long, mean_lat = map_data.latitude.mean(), map_data.longitude.mean()

scl = [0,"rgb(150,0,90)"], [0.125,"rgb(0, 0, 200)"], [0.25,"rgb(0, 25, 255)"],\
[0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
[0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]



app.layout = html.Div(children=[
    html.H1(children='Housing prices in California'),
    
    
    html.Div(children='Please, select min and max median price'),
    dcc.RangeSlider(
        id = 'price_range',
        min = min_house_value,
        max = max_house_value,
        step = (max_house_value-min_house_value)/30,
        value = [min_house_value+(2*(max_house_value-min_house_value)/30), max_house_value-(2*(max_house_value-min_house_value)/30)]
    ),
    html.Div(id='output-container-range-slider'),
    
    html.Div(children='Please, select min and max population'),
    dcc.RangeSlider(
        id = 'population_range',
        min = min_pop,
        max = mean_pop,
        step = (mean_pop - min_pop)/30,
        value = [min_pop+(2*((mean_pop)-min_pop)/30), (mean_pop)-(2*((mean_pop)-min_pop)/30)]
    ),
    html.Div(id='output-pop-slider'),
    
    dcc.RadioItems(
        id = 'loc_choice',
        options=[
            {'label': 'Near Ocean', 'value': 'NEAR OCEAN'},
            {'label': '<1h from Ocean', 'value': '<1H OCEAN'},
            {'label': 'Inland', 'value': 'INLAND'},
            {'label': 'Near San Francisco Bay', 'value': 'NEAR BAY'},
            {'label': 'Island', 'value': 'ISLAND'},
            {'label': 'Whatever', 'value': 'WTVR'}
        ],
        value='WTVR'
    ),

    dcc.Graph(
        id='myMap'
    )
])


#### Callbacks

@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    dash.dependencies.Input('price_range', 'value'))
def update_output(price_range):
    return 'The values are {}'.format(price_range)

@app.callback(
    dash.dependencies.Output('output-pop-slider', 'children'),
    dash.dependencies.Input('population_range', 'value'))
def update_output(pop_range):
    return 'The values are {}'.format(pop_range)

@app.callback(
    dash.dependencies.Output('myMap', 'figure'),
    [dash.dependencies.Input('price_range', 'value'),
    dash.dependencies.Input('loc_choice', 'value'),
    dash.dependencies.Input('population_range', 'value')])
def update_graph(value, location, pop_range):
    
    # Filtering upon price
    filtered_data = map_data[map_data.median_house_value > value[0]]
    filtered_data = filtered_data[filtered_data.median_house_value < value[1]]
    
    # Filtering upon pop
    filtered_data = filtered_data[filtered_data.population > pop_range[0]]
    filtered_data = filtered_data[filtered_data.population < pop_range[1]]

    if location != 'WTVR':
        filtered_data = filtered_data[filtered_data.ocean_proximity == location]

    fig = go.Figure(layout = go.Layout(height = 600, width = 1200),
        data = go.Scattergeo(
        lat = filtered_data['latitude'],
        lon = filtered_data['longitude'],
        text = filtered_data['median_house_value'].astype(str),
        marker = dict(
            color = filtered_data['median_house_value'],
            colorscale = scl,
            reversescale = False,
            opacity = 0.7,
            size = 4,
            colorbar = dict(
                titleside = "right",
                outlinecolor = "rgba(68, 68, 68, 0)",
                ticks = "outside",
                showticksuffix = "last",
                dtick = 50000
                    )
                )
            ))
    
    fig.update_layout(
        geo = dict(
            scope = 'usa',
            showland = True,
            landcolor = "rgb(220, 220, 220)",
            subunitcolor = "rgb(255, 255, 255)",
            countrycolor = "rgb(255, 255, 255)",
            showlakes = True,
            lakecolor = "rgb(255, 255, 255)",
            showsubunits = True,
            showcountries = True,
            resolution = 50,
            center = {'lat': 35, 'lon': -120},
            projection = go.layout.geo.Projection(
                scale=4
            ),
            lonaxis = dict(
                showgrid = True,
                gridwidth = 0.5,
                range= [ -140.0, -55.0 ],
                dtick = 1
            ),
            lataxis = dict(
                showgrid = True,
                gridwidth = 0.5,
                range= [ 20.0, 60.0 ],
                dtick = 1
            )
        ),
        title='Californian housing market',
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)