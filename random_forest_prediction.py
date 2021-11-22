import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, r2_score

class HousePricing:
    
    def __init__(self):
        self.df = self.preprocessing()
        self.X = self.define_X()
        self.y = self.define_y()
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.X, self.y, test_size = 0.25, shuffle=True)

    
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
        model = RandomForestRegressor(n_estimators = 300)
        model.fit(self.X_train, self.y_train)
        return model
    
    def model_validation(self, display_scores=True):
        y_pred = self.model.predict(self.X_val)
        mae = mean_absolute_error(self.y_val, self.y_pred)
        print("Mean absolute error is : {}".format(mae))
        r2 = r2_score(self.y_val, self.y_pred)
        print("R² score is : {}".format(r2))
        return y_pred, mae, r2
        
        