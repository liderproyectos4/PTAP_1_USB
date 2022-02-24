import dash
from dash import dcc
from dash import html

app = dash.Dash()
app.layout = html.Div(
    html.H1(children="Hello world")
)

if __name__=="__main__":
    app.run_server(debug=True)