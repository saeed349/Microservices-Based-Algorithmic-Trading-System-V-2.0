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

# sql="select * from indicator"
# ind_list=list(pd.read_sql(sql,con=conn_indicator)['name'])
# ind_list_id=list(pd.read_sql(sql,con=conn_indicator)['id'])

# sql="select * from indicator"
# df_ind_type=pd.read_sql(sql,con=conn_indicator)

layout = html.Div([
    html.Div(
        [
            html.Div([dcc.Dropdown(id='dropdown-instrument',
                    options=[{'label': i, 'value': i} for i in ['Equity,Forex,Commodities']], multi=False, value="Forex")],
            className='two columns'),
            html.Div([dcc.Dropdown(id='dropdown-timeframe',
                 options=[{'label': i, 'value': i} for i in ['m','w','d','h4','h1','test']], multi=False, value="d")],
            className='two columns'),
            html.Div([
                    dcc.DatePickerSingle(
                    id='date_picker',
                    # min_date_allowed=datetime.datetime(1995, 8, 5),
                    # max_date_allowed=datetime.datetime.now(),
                    # initial_visible_month=datetime.datetime.now(),
                    # display_format='MMMM Y, DD',
                    date=str(datetime.datetime.now().date()))],
            className='four columns'),
    ],className='row'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])



# @app.callback([Output('indicator_table', 'data'),
#               Output('indicator_table', 'columns')],
#               [Input('dropdown-instrument', 'value'),
#               Input('dropdown-timeframe', 'value'),
#               Input('dropdown-indicator', 'value'),
#               Input('date_picker', 'date')])
# def indicator_table(instrument,timeframe,indicator,date):
#     sql="""select * from
#     (
#     select s.ticker, d.value, d.date_price as date,
#     row_number() over(partition by d.symbol_id, d.date_price, d.indicator_id order by d.created_date desc) as rn
#     from {}_data d join symbol s on d.symbol_id=s.id 
#     where s.instrument='{}' and d.indicator_id={} and date_price='{}'
#     ) t
#     where t.rn = 1""".format(timeframe,instrument,indicator,date)
#     df_indicator=pd.read_sql(sql,con=conn_indicator)
#     df_indicator=pd.concat([df_indicator.drop(['value'], axis=1), df_indicator['value'].apply(pd.Series)], axis=1)
#     columns=[{"name": i, "id": i} for i in df_indicator.columns]
#     data=df_indicator.to_dict('records')
#     return data,columns
