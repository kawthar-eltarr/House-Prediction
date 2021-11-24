import dash

BS = "https://raw.githubusercontent.com/eltarr-kawther/House-Prediction/main/assets/style.css"

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[BS])
server = app.server
app.title = "House Prediction"
