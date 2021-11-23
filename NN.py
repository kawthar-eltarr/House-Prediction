## Arthur model NN

import pandas as pd
from zipfile import ZipFile

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


class HousePricing_NN:
    
    def __init__(self):
        self.df = self.preprocessing()
        self.model = self.define_model()
        self.pkl = self.open_pkl()
        self.X = self.define_X()
        self.y = self.define_y()
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.X, self.y, test_size = 0.2, random_state = 42)

    
    def preprocessing(self):
        df = pd.read_csv(r"data/housing.csv")
        df.total_bedrooms.fillna(method='pad', inplace=True)
        label = LabelEncoder()
        df['ocean_proximity'] = label.fit_transform(df['ocean_proximity'])
        return df
    
    def define_model(self):
        inputs = Input(shape = (x_train.shape[1],))

        norm = BatchNormalization(axis = -1,
            momentum = 0.99,
            epsilon = 0.001,
            center = True,
            scale = True,
            beta_initializer = "zeros",
            gamma_initializer = "ones",
            moving_mean_initializer = "zeros",
            moving_variance_initializer = "ones")

        x = norm(inputs)
        x = Dense(32, activation = 'relu')(x)
        x = Dropout(0.2)(x)
        x = Dense(16, activation = 'relu')(x)
        x = Dropout(0.2)(x)
        x = Dense(8, activation = 'relu')(x)
        outputs = Dense(1)(x)

        return keras.Model(inputs=inputs, outputs=outputs, name="housing")
    
    def define_X(self):
        return data.drop('median_house_value', axis=1).astype('float32')
    
    def define_y(self):
        return data.median_house_value
    
    ####
    
    def open_pkl(self):
        pickling_off = open("model/model_nn.pickle","wb")
        pkl = pickle.load(pickling_on)
        pickling_off.close()
        return pkl
    
    def model_train(self):
        def coeff_determination(y_true, y_pred):
            SS_res =  K.sum(K.square( y_true-y_pred )) 
            SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) ) 
            return ( 1 - SS_res/(SS_tot + K.epsilon()) )
        model.compile(
            loss=tf.keras.losses.MeanAbsolutePercentageError(reduction="auto", name="mean_absolute_percentage_error"),
            optimizer=tf.keras.optimizers.Adam(),
            metrics=[coeff_determination]
        )

        history = model.fit(self.X_train, self.y_train, batch_size=256, epochs=100, validation_split=0.4, verbose=0)
        return model
    
    def model_validation(self, display_scores=True):
        test_scores = model.evaluate(self.X_test, self.y_test, verbose=2)
        y_pred = model.predict(self.y_test)
        return y_pred, test_scores[0], test_scores[1]
        
# One-hot encoding of the ocean proximity

for item in list(df.ocean_proximity.unique()):
    df[item] = (df.ocean_proximity == item)

df = df.drop('ocean_proximity', axis=1)
    
for item in list(df_drop.ocean_proximity.unique()):
    df_drop[item] = (df_drop.ocean_proximity == item)

df_drop = df_drop.drop('ocean_proximity', axis=1)
    