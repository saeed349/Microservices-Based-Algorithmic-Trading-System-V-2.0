import psycopg2
import pandas as pd
from plotly.offline import init_notebook_mode, iplot
from plotly.offline import plot 
import plotly.graph_objects as go
import warnings
import datetime
warnings.filterwarnings('ignore')

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# import q_credentials.db_indicator_cred as db_indicator_cred

from app import app

# conn_indicator = psycopg2.connect(host=db_indicator_cred.dbHost , database=db_indicator_cred.dbName, user=db_indicator_cred.dbUser, password=db_indicator_cred.dbPWD)

# sql="select distinct instrument from symbol" # change it to exchange when you reload oanda
# df_instrument_type=pd.read_sql(sql,con=conn_indicator)

layout = html.Div([
    html.Div(
        [
            html.Div([dcc.Dropdown(id='dropdown-instrument',
                    options=[{'label': i, 'value': i} for i in ['Equity,Forex,Commodities']], multi=False, value="Forex")],
            className='two columns'),
            html.Div([dcc.Dropdown(id='dropdown-securities',
                 options=[{'label': i, 'value': i} for i in ['']], multi=False, value="EUR_USD")],
            className='two columns'),
            html.Div([dcc.Dropdown(id='dropdown-timeframe',
                 options=[{'label': i, 'value': i} for i in ['m','w','d','h4','h1','test']], multi=False, value="d")],
            className='two columns'),
            html.Div([
                    dcc.DatePickerSingle(
                    id='date_picker',
                    date=str(datetime.datetime.now().date()))],
            className='four columns'),
    ],className='row'),    
    html.Br(),
    html.Div([
        dcc.Loading(id='loading-1',
        children=[html.Div(dcc.Graph(id="plot-candle"))])
    ],style = {'display': 'inline-block', 'width': '100%','height':'200%'},className='row'),

    dcc.Link('Go back to home', href='/')
])



