import dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html # deprecated
from dash import html
from dash.dependencies import Output, Input

#for layout stuff
import dash_bootstrap_components as dbc

#for data
import pandas as pd

#for plots
import plotly.express as px
import plotly.graph_objects as go

#-------------------------------------------------------------------------------------------------------------------------------------------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

app.layout = dbc.Container([
        dbc.Row([ #First row, 2 columns (logo and line graph)
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src='/assets/yellowcard.png') # 150px by 45px
                ],style={"width": "8rem"}, className='mb-2 border-top-1')
            ],width = 4)
            # dbc.Col([ #don't forget to add back a comma above if you want this section back in
            #     html.H1("Draft Dashboard for Yellow Card", style={'text-align': 'center'}, className = "border-top-2")
            # ])
        ], justify='start'),
        dbc.Row([
            dbc.Col([
                    dcc.Dropdown(id="slct_country",
                    options=[
                        {'label' : 'Nigeria', 'value' : 'Nigeria'},
                        {'label' : 'Thailand', 'value' : 'Thailand'},
                        {'label' : 'Philippines', 'value' : 'Philippines'},
                        {'label' : 'Vietnam', 'value' : 'Vietnam'},
                        {'label' : 'Turkey', 'value' : 'Turkey'},
                        {'label' : 'Argentina', 'value' : 'Argentina'},
                        {'label' : 'South Africa', 'value' : 'South Africa'},
                        {'label' : 'Switzerland', 'value' : 'Switzerland'},
                        {'label' : 'Kenya', 'value' : 'Kenya'},
                        {'label' : 'Malaysia', 'value' : 'Malaysia'},
                        {'label' : 'Brazil', 'value' : 'Brazil'},
                        {'label' : 'Netherlands', 'value' : 'Netherlands'},
                        {'label' : 'Colombia', 'value' : 'Colombia'},
                        {'label' : 'Czechia', 'value' : 'Czechia'},
                        {'label' : 'India', 'value' : 'India'},
                        {'label' : 'Portugal', 'value' : 'Portugal'},
                        {'label' : 'Spain', 'value' : 'Spain'},
                        {'label' : 'Chile', 'value' : 'Chile'},
                        {'label' : 'Pakistan', 'value' : 'Pakistan'},
                        {'label' : 'Ireland', 'value' : 'Ireland'},
                        {'label' : 'United Arab Emirates', 'value' : 'United Arab Emirates'},
                        {'label' : 'United States', 'value' : 'United States'},
                        {'label' : 'Peru', 'value' : 'Peru'},
                        {'label' : 'Hong Kong', 'value' : 'Hong Kong'},
                        {'label' : 'Greece', 'value' : 'Greece'},
                        {'label' : 'South Korea', 'value' : 'South Korea'},
                        {'label' : 'Egypt', 'value' : 'Egypt'},
                        {'label' : 'Indonesia', 'value' : 'Indonesia'},
                        {'label' : 'Saudi Arabia', 'value' : 'Saudi Arabia'},
                        {'label' : 'Australia', 'value' : 'Australia'},
                        {'label' : 'Lithuania', 'value' : 'Lithuania'},
                        {'label' : 'New Zealand', 'value' : 'New Zealand'},
                        {'label' : 'Canada', 'value' : 'Canada'},
                        {'label' : 'Denmark', 'value' : 'Denmark'},
                        {'label' : 'Dominican Republic', 'value' : 'Dominican Republic'},
                        {'label' : 'Serbia', 'value' : 'Serbia'},
                        {'label' : 'Romania', 'value' : 'Romania'},
                        {'label' : 'Singapore', 'value' : 'Singapore'},
                        {'label' : 'Poland', 'value' : 'Poland'},
                        {'label' : 'Morocco', 'value' : 'Morocco'},
                        {'label' : 'Germany', 'value' : 'Germany'},
                        {'label' : 'Mexico', 'value' : 'Mexico'},
                        {'label' : 'Austria', 'value' : 'Austria'},
                        {'label' : 'Taiwan', 'value' : 'Taiwan'},
                        {'label' : 'Belgium', 'value' : 'Belgium'},
                        {'label' : 'Hungary', 'value' : 'Hungary'},
                        {'label' : 'Russia', 'value' : 'Russia'},
                        {'label' : 'Sweden', 'value' : 'Sweden'},
                        {'label' : 'Norway', 'value' : 'Norway'},
                        {'label' : 'Israel', 'value' : 'Israel'},
                        {'label' : 'Italy', 'value' : 'Italy'},
                        {'label' : 'France', 'value' : 'France'},
                        {'label' : 'Finland', 'value' : 'Finland'},
                        {'label' : 'China', 'value' : 'China'},
                        {'label' : 'United Kingdom', 'value' : 'United Kingdom'},
                        {'label' : 'Japan', 'value' : 'Japan'},
                        {'label' : 'Nigeria', 'value' : 'Nigeria'},
                        {'label' : 'Thailand', 'value' : 'Thailand'},
                        {'label' : 'Philippines', 'value' : 'Philippines'},
                        {'label' : 'Vietnam', 'value' : 'Vietnam'}
                        ],
                    multi=True, 
                    value=['Nigeria', 'Morocco', 'Egypt'],
                    style={'width': "100%"}
                    ),
                    #html.Div(id='output_container'), #nothing is in the children spot yet

                    dbc.CardBody(id = 'output_component'),

                    #html.Br(),
                    dcc.Graph(id='crypto_use_line_graph', figure={}, config={'displayModeBar':False}, className = "border-top-1"
                )
            ], width = 12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="/assets/bitcoin.png",
                            top=True, 
                            style={"width": "4rem"},
                            className="ml-3"),
                        dbc.CardBody([
                            dbc.Row([
                                
                                dbc.Col([
                                    html.P("CHANGE (1D)", className="ml-3")
                                ],width={'size':5, 'offset':1}),

                                dbc.Col([
                                    dcc.Graph(id='bit_indicator-graph', figure={},
                                            config={'displayModeBar':False},
                                            )
                                ], width={'size':5,'offset':1})
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(id='bit_daily-line', figure={},
                                            config={'displayModeBar':False})
                                ], width=12),

                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dbc.Label(id='bit_latest-price', children = [],
                                            className="mt-2 ml-5 bg-white p-1 border border-primary border-top-1")
                                ],width=10)
                            ],justify = 'center')
                        ]),
                    ],
                    style={"width": "24rem"},
                    className="mt-3"
                )
            ], width=4),
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="/assets/ethereum.png",
                            top=True, 
                            style={"width": "3rem"},
                            className="ml-3"),
                        dbc.CardBody([
                            dbc.Row([
                                
                                dbc.Col([
                                    html.P("CHANGE (1D)", className="ml-3")
                                ],width={'size':5, 'offset':1}),

                                dbc.Col([
                                    dcc.Graph(id='eth_indicator-graph', figure={},
                                            config={'displayModeBar':False},
                                            )
                                ], width={'size':5,'offset':1})
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(id='eth_daily-line', figure={},
                                            config={'displayModeBar':False})
                                ], width=12),

                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dbc.Label(id='eth_latest-price', children = [],
                                            className="mt-2 ml-5 bg-white p-1 border border-primary border-top-1")
                                ],width=10)
                            ],justify = 'center')
                        ]),
                    ],
                    style={"width": "24rem"},
                    className="mt-3"
                )
            ], width = 4), 
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="/assets/tether.png",
                            top=True, 
                            style={"width": "8rem"},
                            className="ml-3"),
                        dbc.CardBody([
                            dbc.Row([
                                
                                dbc.Col([
                                    html.P("CHANGE (1D)", className="ml-3")
                                ],width={'size':5, 'offset':1}),

                                dbc.Col([
                                    dcc.Graph(id='usdt_indicator-graph', figure={},
                                            config={'displayModeBar':False},
                                            )
                                ], width={'size':5,'offset':1})
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(id='usdt_daily-line', figure={},
                                            config={'displayModeBar':False})
                                ], width=12),

                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dbc.Label(id='usdt_latest-price', children = [],
                                            className="mt-2 ml-5 bg-white p-1 border border-primary border-top-1")
                                ],width=10)
                            ],justify = 'center')
                        ]),
                    ],
                    style={"width": "24rem"},
                    className="mt-3"
                )
            ], width=4)
        ], justify='center'),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id = 'crypto_map', figure = {}, className = "mt-2 border-top-1")
            ],width = 12)
        ],justify = 'center'),
    dcc.Interval(id='update', n_intervals=0, interval=1000*5)
])

#Crypto Line Graph -----------------------------------------------------------------------------------------------------------------
line_data = pd.read_csv("data/world_crypto_usage2.csv")


@app.callback( #connect compenents with graph
    [Output(component_id='crypto_use_line_graph', component_property='children'), #two outputs, one the children out the output container, and also the figure of the compenent id my_bee_map
    Output(component_id='crypto_use_line_graph', component_property='figure')],
    Input(component_id='slct_country', component_property='value')
)

def update_graph(slct_country):

    container = "Country or countries chosen: {}".format(slct_country)

    fig = px.line(
    data_frame=line_data[line_data['Country'].isin(slct_country)],
    x = 'Year',
    y = 'Usage',
    color = 'Country',
    title = 'Percent of the Pop Using Crypto (at least once per year)',
    #template = 'plotly_dark'    
    )

    fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                   xaxis_title='Year',
                   yaxis_title='Usage (%)')
    return container, fig

########################################################### Bitcoin Section ####################################################################


#Import Bitcoin Data ---------------------------------------------------------------------------------------------------------------
bitcoin = pd.read_csv("data/bitcoin.csv")
btc = bitcoin.copy()
btc.reset_index(inplace=True)

#Bitcoin Price Label -------------------------------------------------------------------------------------------------------------------------
@app.callback(
    [Output('bit_latest-price', 'children'),
    Output('bit_latest-price', 'className')],
    Input('update', 'n_intervals')
)

def update_graph(timer):
    # #Get latest price
    day_end = btc[btc['Datetime'] == btc['Datetime'].max()]['Close'].values[0]
    
    #Get the latest date and convert to nice string format
    # date =  pd.to_datetime(btc['Datetime'].max().date()) 
    # day = date.day
    # month = date.month
    # year = date.year

    # #Get month name, not number 
    # months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # month_name = months_in_year [month - 1]
    # date_final = str(month_name) +' '+ str(day)+ ', ' + str(year)

    return "{} USD".format(round(day_end,2)), "mt-2 bg-white p-1 border border-primary border-top-1"
    


# BitCoin Indicator Graph ----------------------------------------------------------------------------------------------------------

@app.callback(
    Output('bit_indicator-graph', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    #dff_rv = dff.iloc[::-1]
    day_start = btc[btc['Datetime'] == btc['Datetime'].min()]['Close'].values[0]
    day_end = btc[btc['Datetime'] == btc['Datetime'].max()]['Close'].values[0]

    fig = go.Figure(go.Indicator(
        mode="delta",
        value=day_end,
        delta={'reference': day_start, 'relative': True, 'valueformat':'.2%'}))
    fig.update_traces(delta_font={'size':12})
    fig.update_layout(height=30, width=70)

    if day_end >= day_start:
        fig.update_traces(delta_increasing_color='green')
    elif day_end < day_start:
        fig.update_traces(delta_decreasing_color='red')

    return fig

#Line Graph -------------------------------------------------------------------------------------------
@app.callback(
    Output('bit_daily-line', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    #dff_rv = dff.iloc[::-1]
    fig = px.line(btc, x='Datetime', y='Close',
                    range_y=[btc['Close'].min(), btc['Close'].max()],
                    height=120).update_layout(margin=dict(t=0, r=0, l=0, b=20),
                                                paper_bgcolor='rgba(0,0,0,0)',
                                                plot_bgcolor='rgba(0,0,0,0)',
                                                yaxis=dict(
                                                title=None,
                                                showgrid=False,
                                                showticklabels=False
                                                ),
                                                xaxis=dict(
                                                title=None,
                                                showgrid=False,
                                                showticklabels=False
                                                ))

    day_start = btc[btc['Datetime'] == btc['Datetime'].min()]['Close'].values[0]
    day_end = btc[btc['Datetime'] == btc['Datetime'].max()]['Close'].values[0]

    if day_end >= day_start:
        return fig.update_traces(fill='tozeroy',line={'color':'green'})
    elif day_end < day_start:
        return fig.update_traces(fill='tozeroy',
                                line={'color': 'red'})

########################################################### End Bitcoin Section ####################################################################


########################################################### Ethereum Section #######################################################################
#Import Ethereum Data ---------------------------------------------------------------------------------------------------------------
ethereum = pd.read_csv("data/ethereum.csv")
eth = ethereum.copy()
eth.reset_index(inplace=True)

#Ethereum Price Label -------------------------------------------------------------------------------------------------------------------------
@app.callback(
    [Output('eth_latest-price', 'children'),
    Output('eth_latest-price', 'className')],
    Input('update', 'n_intervals')
)

def update_graph(timer):
    #Get latest price
    day_end = eth[eth['Datetime'] == eth['Datetime'].max()]['Close'].values[0]
    return "{} USD".format(round(day_end,2)), "mt-2 bg-white p-1 border border-primary border-top-1"
    


# Ethereum Indicator Graph ----------------------------------------------------------------------------------------------------------

@app.callback(
    Output('eth_indicator-graph', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    #dff_rv = dff.iloc[::-1]
    day_start = eth[eth['Datetime'] == eth['Datetime'].min()]['Close'].values[0]
    day_end = eth[eth['Datetime'] == eth['Datetime'].max()]['Close'].values[0]

    fig = go.Figure(go.Indicator(
        mode="delta",
        value=day_end,
        delta={'reference': day_start, 'relative': True, 'valueformat':'.2%'}))
    fig.update_traces(delta_font={'size':12})
    fig.update_layout(height=30, width=70)

    if day_end >= day_start:
        fig.update_traces(delta_increasing_color='green')
    elif day_end < day_start:
        fig.update_traces(delta_decreasing_color='red')

    return fig

#Line Graph -------------------------------------------------------------------------------------------
@app.callback(
    Output('eth_daily-line', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    #dff_rv = dff.iloc[::-1]
    fig = px.line(eth, x='Datetime', y='Close',
                    range_y=[eth['Close'].min(), eth['Close'].max()],
                    height=120).update_layout(margin=dict(t=0, r=0, l=0, b=20),
                                                paper_bgcolor='rgba(0,0,0,0)',
                                                plot_bgcolor='rgba(0,0,0,0)',
                                                yaxis=dict(
                                                title=None,
                                                showgrid=False,
                                                showticklabels=False
                                                ),
                                                xaxis=dict(
                                                title=None,
                                                showgrid=False,
                                                showticklabels=False
                                                ))

    day_start = eth[eth['Datetime'] == eth['Datetime'].min()]['Close'].values[0]
    day_end = eth[eth['Datetime'] == eth['Datetime'].max()]['Close'].values[0]

    if day_end >= day_start:
        return fig.update_traces(fill='tozeroy',line={'color':'green'})
    elif day_end < day_start:
        return fig.update_traces(fill='tozeroy',
                                line={'color': 'red'})

########################################################### End Ethereum Section #######################################################################

########################################################### Tether Section #######################################################################
#Import Tether Data ---------------------------------------------------------------------------------------------------------------
tether = pd.read_csv("data/tether.csv")
usdt = tether.copy()
usdt.reset_index(inplace=True)

#Ethereum Price Label -------------------------------------------------------------------------------------------------------------------------
@app.callback(
    [Output('usdt_latest-price', 'children'),
    Output('usdt_latest-price', 'className')],
    Input('update', 'n_intervals')
)

def update_graph(timer):
    #Get latest price
    day_end = usdt[usdt['Datetime'] == usdt['Datetime'].max()]['Close'].values[0]
    return "{} USD".format(round(day_end,2)), "mt-2 bg-white p-1 border border-primary border-top-1"
    


# Tether Indicator Graph ----------------------------------------------------------------------------------------------------------

@app.callback(
    Output('usdt_indicator-graph', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    day_start = usdt[usdt['Datetime'] == usdt['Datetime'].min()]['Close'].values[0]
    day_end = usdt[usdt['Datetime'] == usdt['Datetime'].max()]['Close'].values[0]

    fig = go.Figure(go.Indicator(
        mode="delta",
        value=day_end,
        delta={'reference': day_start, 'relative': True, 'valueformat':'.2%'}))
    fig.update_traces(delta_font={'size':12})
    fig.update_layout(height=30, width=70)

    if day_end >= day_start:
        fig.update_traces(delta_increasing_color='green')
    elif day_end < day_start:
        fig.update_traces(delta_decreasing_color='red')

    return fig

#Line Graph -------------------------------------------------------------------------------------------
@app.callback(
    Output('usdt_daily-line', 'figure'),
    Input('update', 'n_intervals')
)
def update_graph(timer):
    fig = px.line(usdt, x='Datetime', y='Close',
                    range_y=[usdt['Close'].min(), usdt['Close'].max()],
                    height=120).update_layout(margin=dict(t=0, r=0, l=0, b=20),
                                                paper_bgcolor='rgba(0,0,0,0)',
                                                plot_bgcolor='rgba(0,0,0,0)',
                                                yaxis=dict(
                                                title=None,
                                                showgrid=False,
                                                showticklabels=False
                                                ),
                                                xaxis=dict(
                                                title=None,
                                                showgrid=False,
                                                showticklabels=False
                                                ))

    day_start = usdt[usdt['Datetime'] == usdt['Datetime'].min()]['Close'].values[0]
    day_end = usdt[usdt['Datetime'] == usdt['Datetime'].max()]['Close'].values[0]

    if day_end >= day_start:
        return fig.update_traces(fill='tozeroy',line={'color':'green'})
    elif day_end < day_start:
        return fig.update_traces(fill='tozeroy',
                                line={'color': 'red'})

########################################################### End Tether Section #######################################################################


########################################################### Crypto Ownership Map #####################################################################

df = pd.read_csv("data/world_crypto_ownership.csv")

@app.callback(
    Output('crypto_map', 'figure'),
    Input('update', 'n_intervals')
)

def update_graph(timer):
    fig = px.choropleth(
        data_frame = df,
        #locationmode='country names',
        locations='iso_3',
        #scope = 'world',
        color = "Percentage of the population",
        projection='natural earth',
        hover_data=["Number of crypto owners", "Percentage of the population"],
        #color_continuous_scale=px.colors.sequential.OrRd,
        labels = {'Percentage of the population' : 'Population'},
        title = 'Crypocurrency Owernship Globally',
        template='plotly_dark'
    )


    fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                            margin=dict(l=60, r=60, t=50, b=50))
    return fig

########################################################### End Crypto Ownership Map ################################################################

if __name__=='__main__':
    app.run_server(debug=True, port=8000)