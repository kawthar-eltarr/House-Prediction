import numpy as np
from dash.dependencies import Input, Output, State

from sklearn.preprocessing import StandardScaler

import joblib

from app import app

@app.callback(Output('output-prediction', 'children'),
              Input('submit-val', 'n_clicks'),
              Input('input-form-longitude', 'value'), 
              Input('input-form-latitude', 'value'),
              Input('input-form-median-age', 'value'),
              Input('input-form-rooms', 'value'),
              Input('input-form-bedrooms', 'value'),
              Input('input-form-population', 'value'),
              Input('input-form-households', 'value'),
              Input('input-form-income', 'value'),
              Input('input-form-proximity', 'value'))
def update_output(n_clicks, input1, input2, input3, input4, input5,
                  input6, input7, input8, input9):
    
    if input1 and input2 and input3 and input4 and input5 and input6 and input7 and input8 and input9:
        X_test = np.array([float(input1), float(input2), float(input3), float(input4), float(input5),
                           float(input6), float(input7), float(input8), input9]).reshape(1, -1)
    
        scaler = StandardScaler()
        
        scaler.fit_transform(X_test)
        
        regressor = joblib.load('model/RF_model.sav') 
        
        y_pred = regressor.predict(X_test)
        
        return '{}'.format(y_pred)
