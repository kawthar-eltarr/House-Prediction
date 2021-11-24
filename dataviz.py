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
map_data = df[
    ['longitude', 'latitude', 'median_house_value', 'ocean_proximity', 'population', 'total_rooms', 'total_bedrooms',
     'households']]

# Taking random data to test the map
rnd = np.random.randint(0, df.shape[0], 5000)
map_data = map_data.iloc[rnd, :]

#### Layout

# Getting data
max_house_value, min_house_value = map_data.median_house_value.max(), map_data.median_house_value.min()

max_pop, min_pop, std_pop = map_data.population.max(), map_data.population.min(), map_data.population.std()
mean_pop = map_data.population.mean()

mean_long, mean_lat = map_data.latitude.mean(), map_data.longitude.mean()

map_data['mean_rooms'] = map_data.total_rooms / map_data.households
max_mean_rooms, min_mean_rooms = map_data.mean_rooms.max(), map_data.mean_rooms.min()

map_data['mean_bedrooms'] = map_data.total_bedrooms / map_data.households
max_mean_bedrooms, min_mean_bedrooms = map_data.mean_bedrooms.max(), map_data.mean_bedrooms.min()

scl = [0, "rgb(150,0,90)"], [0.125, "rgb(0, 0, 200)"], [0.25, "rgb(0, 25, 255)"], \
      [0.375, "rgb(0, 152, 255)"], [0.5, "rgb(44, 255, 150)"], [0.625, "rgb(151, 255, 0)"], \
      [0.75, "rgb(255, 234, 0)"], [0.875, "rgb(255, 111, 0)"], [1, "rgb(255, 0, 0)"]


def mark_list(var1, var2, k=5, r=2):
    '''Returns a list to be used as marker generator'''
    if r == 0:
        return [round(var1 + i * (var2 - var1) / k) for i in range(k)]
    return [round(var1 + i * (var2 - var1) / k, r) for i in range(k)]


max_mean_rooms /= 5
max_mean_bedrooms /= 5

app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Housing prices in California'),

        html.H4(id='mean_price', style={'text-decoration': 'underline'}),

        html.Div(
            html.Div(
                html.P(
                    [
                        html.H4('Type of graph'),
                        dcc.Dropdown(
                            id='dropdown_graph',
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

                        # to be exponential
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
                            value='WTVR'
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


#### Callbacks

@app.callback(
    [dash.dependencies.Output('myMap', 'figure'),
     dash.dependencies.Output('mean_price', 'children')],
    [dash.dependencies.Input('price_range', 'value'),
     dash.dependencies.Input('loc_choice', 'value'),
     dash.dependencies.Input('population_range', 'value'),
     dash.dependencies.Input('mean_rooms', 'value'),
     dash.dependencies.Input('mean_bedrooms', 'value'),
     dash.dependencies.Input('dropdown_graph', 'value')])
def update_data(value, location, pop_range, room_range, bedroom_range, graph):
    # Filtering upon price
    global fig
    filtered_data = map_data[map_data.median_house_value > value[0]]
    filtered_data = filtered_data[filtered_data.median_house_value < value[1]]

    # Filtering upon pop
    filtered_data = filtered_data[filtered_data.population > pop_range[0]]
    filtered_data = filtered_data[filtered_data.population < pop_range[1]]

    # Filtering upon mean rooms
    filtered_data = filtered_data[filtered_data.mean_rooms > room_range[0]]
    filtered_data = filtered_data[filtered_data.mean_rooms < room_range[1]]

    # Filtering upon mean bedrooms
    filtered_data = filtered_data[filtered_data.mean_bedrooms > bedroom_range[0]]
    filtered_data = filtered_data[filtered_data.mean_bedrooms < bedroom_range[1]]

    if location != 'WTVR':
        filtered_data = filtered_data[filtered_data.ocean_proximity == location]

    if graph == 'map':
        fig = go.Figure(layout=go.Layout(height=500, width=700),
                        data=go.Scattergeo(
                            lat=filtered_data['latitude'],
                            lon=filtered_data['longitude'],
                            text=filtered_data['median_house_value'].astype(str),
                            marker=dict(
                                color=filtered_data['median_house_value'],
                                colorscale=scl,
                                reversescale=False,
                                opacity=0.7,
                                size=4,
                                colorbar=dict(
                                    titleside="right",
                                    outlinecolor="rgba(68, 68, 68, 0)",
                                    ticks="outside",
                                    showticksuffix="last",
                                    dtick=50000
                                )
                            )
                        ))

        fig.update_layout(
            geo=dict(
                scope='usa',
                showland=True,
                landcolor="rgb(220, 220, 220)",
                subunitcolor="rgb(255, 255, 255)",
                countrycolor="rgb(255, 255, 255)",
                showlakes=True,
                lakecolor="rgb(255, 255, 255)",
                showsubunits=True,
                showcountries=True,
                resolution=50,
                center={'lat': 35, 'lon': -120},
                projection=go.layout.geo.Projection(
                    scale=4
                ),
                lonaxis=dict(
                    showgrid=True,
                    gridwidth=0.5,
                    range=[-140.0, -55.0],
                    dtick=1
                ),
                lataxis=dict(
                    showgrid=True,
                    gridwidth=0.5,
                    range=[20.0, 60.0],
                    dtick=1
                )
            )
        )

    # Creating mean value text

    if graph == 'hist':
        fig = px.histogram(filtered_data, x="median_house_value",
                           nbins=100,
                           labels={'x': 'Median House Value', 'y': ''},
                           histnorm='percent')

    mean_value = filtered_data.median_house_value.mean()

    if mean_value is np.nan:
        mean_median_price_text = 'There are no house in the selection !'
    else:
        mean_median_price_text = 'The mean price is {}'.format(round(mean_value, 2))

    return fig, mean_median_price_text


if __name__ == '__main__':
    app.run_server(debug=True)
