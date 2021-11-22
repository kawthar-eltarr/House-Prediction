import dash

BS = r"C:/Users/straw/Desktop/AIS2/House-Prediction/assets/style.css"

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[BS])
server = app.server
app.title = "House Prediction"
