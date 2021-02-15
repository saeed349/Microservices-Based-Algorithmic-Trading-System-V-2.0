import dash

external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets
)

server = app.server