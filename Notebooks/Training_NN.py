## Arthur model NN

import keras
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns
import kaggle
from zipfile import ZipFile

# Data extract
zf = ZipFile('archive.zip')
zf.extractall('data/') #save files in selected folder
zf.close()

df = pd.read_csv('data/housing.csv')
df.head(10)

class model(self):
    self.y = y
    self.x = x
    self.data = 
    