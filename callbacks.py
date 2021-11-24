import numpy as np
from dash.dependencies import Input, Output, State

from app import app
@app.callback(Output('output-prediction', 'children'),
              Input('submit-val', 'n_clicks'),
              State('input-form-longitude', 'value'), 
              State('input-form-latitude', 'value'),
              State('input-form-median-age', 'value'),
              State('input-form-rooms', 'value'),
              State('input-form-bedrooms', 'value'),
              State('input-form-population', 'value'),
              State('input-form-households', 'value'),
              State('input-form-income', 'value'),
              State('input-form-house-value', 'value'),
              State('input-form-proximity', 'value'))
def update_output(n_clicks, input1, input2, input3, input4, input5,
                  input6, input7, input8, input9, input10):

    X_test = np.array([input1, input2, input3, input4, input5, input6,
                       input7, input8, input9, input10]).reshape(1, -1)
    #regr3.predict(X_test)
    return '{}'.format(X_test)
