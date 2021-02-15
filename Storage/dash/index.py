import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app_individual, app_aggregate

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page  = html.Div([
    dcc.Link('Individual Analysis', href='/individual'),
    html.Br(),
    dcc.Link('Agregrate Analysis', href='/agregrate'),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/individual':
        return app_individual.layout
    elif pathname == '/agregrate':
        return app_aggregate.layout
    else:
        return index_page



if __name__=="__main__":
    # app.run_server(debug=True, port=5001)
    app.run_server(
        host='0.0.0.0',
        port=8050,
        debug=True
    )