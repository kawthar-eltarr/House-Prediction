from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from app import server
from layouts import layout1, layout2, layout3, layout4, layout5
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
         return layout1
    elif pathname == '/pred_tool':
         return layout2
    elif pathname == '/pred_tool/ml':
         return layout3
    elif pathname == '/pred_tool/dl':
         return layout4
    elif pathname == '/viz_tool':
         return layout5
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
