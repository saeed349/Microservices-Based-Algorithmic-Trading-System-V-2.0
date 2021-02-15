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

# @app.callback(
#     Output('dropdown-securities', 'options'),
#     [Input('dropdown-instrument', 'value')]
# )
# def update_tickerdropdown(instrument_type):
#     # return none
#     sql="""select * from (select symbol_id, min(date_price), max(date_price) from d_data group by symbol_id) a join symbol s
#     on s.id=a.symbol_id where s.instrument='{}' """.format(instrument_type)
#     df_ticker_last_day=pd.read_sql(sql,con=conn_indicator)
#     return [{'label': i, 'value': i} for i in df_ticker_last_day['ticker'].unique()]

# @app.callback(
#     Output('plot-candle', 'figure'),
#     [Input('dropdown-securities', 'value'),
#     Input('dropdown-timeframe','value'),
#     Input('date_picker', 'date')]
# )
# def updatePlot(symbol,timeframe,date):
    
#     interested_feature='anomaly_gap_dev'#'anomaly_vol_anomaly'
#     df=data_selector(symbol,timeframe)

#     df_candle_1=df[-10:]
#     df_candle_1=df_candle_1[df_candle_1['candle_1_pattern_name']!='']
#     df_candle_1['pattern']='1'

#     df_candle_2=df[-10:]
#     df_candle_2=df_candle_2[df_candle_2['candle_2_pattern_name']!='']
#     df_candle_2['pattern']='2'

#     df_candle_3=df[-10:]
#     df_candle_3=df_candle_3[df_candle_3['candle_3_pattern_name']!='']
#     df_candle_3['pattern']='3'
    
#     data = [ dict(
#     type = 'candlestick',
#     open = df.open,
#     high = df.high,
#     low = df.low,
#     close = df.close,
#     x = df.index,
#     yaxis = 'y1',
#     name = 'price'
#     )]
    

#     data.append( dict( x=df.index, y=df.volume,                         
#                              marker=dict( color='blue' ),
#                              type='bar', yaxis='y2', name='Volume'))

#     data.append( dict( x=df.index, y=df[interested_feature],                         
#                              marker=dict( color='red' ),
#                              type='scatter', yaxis='y3', name=interested_feature))

#     data.append( dict( x=df_candle_1.index, y=df_candle_1['high'],
#                              text=df_candle_1['pattern'],
#                              mode="markers+text",textfont_size=15,textposition="top center",
#                              marker=dict( color='blue' ),
#                              type='scatter', yaxis='y1', name='candle_patter_1'))

#     data.append( dict( x=df_candle_2.index, y=df_candle_2['high'],
#                              text=df_candle_2['pattern'],
#                              mode="markers+text",textfont_size=15,textposition="top center",
#                              marker=dict( color='red' ),
#                              type='scatter', yaxis='y1', name='candle_patter_2'))


#     data.append( dict( x=df_candle_3.index, y=df_candle_3['high'],
#                              text=df_candle_3['pattern'],
#                              mode="markers+text",textfont_size=15,textposition="top center",
#                              marker=dict( color='red' ),
#                              type='scatter', yaxis='y1', name='candle_patter_3'))


#     layout=dict()    
#     layout['xaxis'] = dict( rangeslider = dict( visible = False ),autorange=True,fixedrange=False,visible=False,type='category')#type='category',
#     layout['yaxis'] = dict( domain = [0.2, 1],autorange = True,fixedrange=False)
#     layout['yaxis2'] = dict( domain = [0.0, 0.1],autorange = True,fixedrange=False)
#     layout['yaxis3'] = dict( domain = [0.1, 0.2],autorange = True,fixedrange=False)
#     layout['shapes'] = level_plot(df,date)
#     layout['margin']=dict(l=20, r=10)
#     layout['paper_bgcolor']="LightSteelBlue"
#     layout['width']=2200
#     layout['height']=1000
#     # to add the crosshair
#     layout['xaxis']['showspikes']=True
#     layout['xaxis']['spikemode']  = 'across'
#     layout['xaxis']['spikesnap'] = 'cursor'
#     fig = dict( data=data, layout=layout )
#     return fig


# def level_plot(df,level_date):
#     level_date=datetime.datetime.strptime(level_date,'%Y-%m-%d') 
#     if df.index[-1]<level_date:
#         level_date=df.index[-1]
#     try:
#         support_ls = [[ls[0],ls[1],datetime.datetime.strptime(ls[2],'%Y-%m-%d %H:%M:%S'),ls[3]] for ls in df.loc[level_date]['level_support']]
#     except:
#         support_ls =[]
#     try:
#         resistance_ls = [[ls[0],ls[1],datetime.datetime.strptime(ls[2],'%Y-%m-%d %H:%M:%S'),ls[3]] for ls in df.loc[level_date]['level_resistance']]
#     except:
#         resistance_ls =[]
#     end_dt=level_date
#     res_plot_ls=[]
#     sup_plot_ls=[]
#     for res in resistance_ls[:5]:
#         res_plot_ls.append(dict(x0=res[2],x1=end_dt,y0=res[0],y1=res[1],yref='y1',opacity=.2,fillcolor='Red',line=dict(color="black",width=1)))
#     for sup in support_ls[:5]:
#         sup_plot_ls.append(dict(x0=sup[2],x1=end_dt,y0=sup[0],y1=sup[1],yref='y1',opacity=.2,fillcolor='green',line=dict(color="black",width=1)))
#     return (res_plot_ls+sup_plot_ls)

# def data_selector(symbol,timeframe):
#     sql="select * from indicator"
#     ind_list=list(pd.read_sql(sql,con=conn_indicator)['name'])
#     start_date=datetime.datetime(2016,1,1).strftime("%Y-%m-%d")
    
#     df_all_ind=pd.DataFrame()
#     for ind in ind_list:
#         print(ind)
#         sql="""select * from
#         (
#         select d.date_price as date,d.value, 
#         row_number() over(partition by d.date_price, d.symbol_id, d.indicator_id order by d.created_date desc) as rn
#         from {}_data d join symbol s on d.symbol_id = s.id join indicator i on i.id=d.indicator_id 
#         where s.ticker='{}' and i.name = '{}' and d.date_price > '{}'   
#         ) t
#         where t.rn = 1""".format(timeframe, symbol, ind, start_date)

#         df_indicator=pd.read_sql(sql,con=conn_indicator)
#         df_indicator.set_index('date',inplace=True)
#         df_indicator=pd.concat([df_indicator.drop(['value'], axis=1), df_indicator['value'].apply(pd.Series)], axis=1)
#         df_indicator.columns=[ind+"_"+col for col in df_indicator.columns]
#         # df_indicator.to_csv(('data/'+ind+'.csv'))
#         if df_all_ind.empty:
#             df_all_ind=df_indicator
#         elif not df_indicator.empty:
#             df_all_ind=pd.merge(left=df_all_ind, right=df_indicator,on='date')
#             # df_all_ind.to_csv(('data/final'+ind+'.csv'))
#         else:
#             pass
#     df_all_ind.rename(columns={'anomaly_close':'close','anomaly_low':'low','anomaly_high':'high','anomaly_open':'open','anomaly_volume':'volume'},inplace=True)
#     # df_all_ind.set_index('date',inplace=True)
#     # df_all_ind.to_csv("data/dash_final_indicators.csv")
#     df_all_ind.sort_values(by=['date'],inplace=True) # because the candlestick plotly figure consider the date as categorical
#     return df_all_ind


