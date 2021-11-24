import numpy as np
import pandas as pd
# Plotly
import plotly.graph_objects as go
import plotly.express as px

from dash.dependencies import Input, Output

from sklearn.preprocessing import StandardScaler

import joblib

import keras

from app import app


# Getting data
df = pd.read_csv('housing.csv')
map_data = df[
    ['longitude', 'latitude', 'median_house_value', 'ocean_proximity', 'population', 'total_rooms', 'total_bedrooms',
     'households']]

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


@app.callback(Output('output-prediction-ml', 'children'),
              Input('submit-val-ml', 'n_clicks'),
              Input('input-form-longitude', 'value'),
              Input('input-form-latitude', 'value'),
              Input('input-form-median-age', 'value'),
              Input('input-form-rooms', 'value'),
              Input('input-form-bedrooms', 'value'),
              Input('input-form-population', 'value'),
              Input('input-form-households', 'value'),
              Input('input-form-income', 'value'),
              Input('input-form-proximity', 'value'))
def update_output_ml(n_clicks, input1, input2, input3, input4, input5,
                  input6, input7, input8, input9):
    if input1 and input2 and input3 and input4 and input5 and input6 and input7 and input8 and input9:
        X_test = np.array([float(input1), float(input2), float(input3), float(input4), float(input5),
                           float(input6), float(input7), float(input8), input9]).reshape(1, -1)

        scaler = StandardScaler()

        scaler.fit_transform(X_test)

        regressor = joblib.load('model/RF_model.sav')

        y_pred = regressor.predict(X_test)

        return '{}'.format(y_pred)

@app.callback(Output('output-prediction-dl', 'children'),
              Input('submit-val-dl', 'n_clicks'),
              Input('input-form-longitude', 'value'),
              Input('input-form-latitude', 'value'),
              Input('input-form-median-age', 'value'),
              Input('input-form-rooms', 'value'),
              Input('input-form-bedrooms', 'value'),
              Input('input-form-population', 'value'),
              Input('input-form-households', 'value'),
              Input('input-form-income', 'value'),
              Input('input-form-proximity', 'value'))
def update_output_dl(n_clicks, input1, input2, input3, input4, input5,
                  input6, input7, input8, input9):
    if input1 and input2 and input3 and input4 and input5 and input6 and input7 and input8 and input9:
        X_test = np.array([float(input1), float(input2), float(input3), float(input4), float(input5),
                           float(input6), float(input7), float(input8), input9]).reshape(1, -1)

        scaler = StandardScaler()

        scaler.fit_transform(X_test)

        model = keras.models.load_model(r'C:/Users/straw/Desktop/AIS2/House-Prediction/model/nn_model')

        y_pred = model.predict(X_test)

        return '{}'.format(y_pred)

@app.callback(
    [Output('myMap', 'figure'),
     Output('mean_price', 'children')],
    [Input('price_range', 'value'),
     Input('loc_choice', 'value'),
     Input('population_range', 'value'),
     Input('mean_rooms', 'value'),
     Input('mean_bedrooms', 'value'),
     Input('dropdown_graph', 'value')])
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
