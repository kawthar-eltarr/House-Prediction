import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, r2_score

import joblib

class HousePricing:
    
    def __init__(self):
        self.df = self.preprocessing()
        self.X = self.define_X()
        self.y = self.define_y()
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.X, self.y, test_size = 0.25, shuffle=True)
        self.model = None

    
    def preprocessing(self):
        
        df = pd.read_csv(r"C:/Users/straw/Desktop/AIS2/House-Prediction/Data/housing.csv")
        
        df.total_bedrooms.fillna(method='pad', inplace=True)
        
        label = LabelEncoder()

        df['ocean_proximity'] = label.fit_transform(df['ocean_proximity'])
        
        return df
    
    def define_X(self):
        X = np.array(self.df.loc[:, ~self.df.columns.isin(['median_house_value'])])
        scaler = StandardScaler()
        return scaler.fit_transform(X)
    
    def define_y(self):
        return np.array(self.df["median_house_value"])
    
    def model_train(self):
        self.model = RandomForestRegressor(n_estimators = 300)
        self.model.fit(self.X_train, self.y_train)
        return self.model
    
    def model_validation(self, display_scores=True):
        y_pred = self.model.predict(self.X_val)
        mae = mean_absolute_error(self.y_val, y_pred)
        r2 = r2_score(self.y_val, y_pred)
        if display_scores:
            print("Mean absolute error is : {}".format(mae))
            print("R² score is : {}".format(r2))
        return y_pred, mae, r2
    
    def model_overall(self, display_scores=True):
        y_pred = self.model.predict(self.X)
        mae = mean_absolute_error(self.y, y_pred)
        r2 = r2_score(self.y, y_pred)
        if display_scores:
            print("Mean absolute error is : {}".format(mae))
            print("R² score is : {}".format(r2))
        return y_pred, mae, r2

    def save_model(self):
        filename = 'model\RF_model.sav'
        joblib.dump(self.model, filename)
        
    def model_predict(self, X_test):
        scaler = StandardScaler()
        scaler.fit_transform(X_test)
        return self.model.predict(X_test)
        
        

if __name__ == '__main__':
    hp = HousePricing()
    hp.model_train()
    hp.model_validation()
    hp.model_overall()
    hp.save_model()
    
        
        