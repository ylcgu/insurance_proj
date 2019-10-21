
    dcc.Graph(
        id='volume',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['ticker'] == i]['High'],
                    y=df[df['ticker'] == i]['Volume'],
                    text=df[df['ticker'] == i]['Date'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'High'},
                yaxis={'title': 'Volume'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
    ]),




html.Br(),
   #html.H6('STOCK MARKET TICKERS'),
   html.H6(
   children = 'try some graph',
   ),
   # dcc.Dropdown(
   #     id= 'k-drop',
   #     options =[{'label':'Apple', 'value':'AAPL'},
   #              {'label': 'Ford', 'value':'F'},
   #              {'label': 'Advanced Micro Devices', 'value': 'AMD'},
   #              {'label': 'Bank of America', 'value': 'BAC'},
   #              {'label': 'GE', 'value': 'GE'}
   #     ],
   #     #options =[{'label': i, 'value': 1} for i in [5,10,15,20,25]],
   #     value='AAPL',
   #     ),
   #     html.Div(id='output-message'),
   #     html.Br(),

   dcc.Graph(
       id='volume',
       figure={
           'data': [
               go.Bar(x = results2.loc['female'].index,
                                y = results2.loc['female']['expenses'],
                                name = 'female',
                                )
                                 for i in df.ticker.unique()
           ],
              go.Bar(x = results2.loc['male'].index,
                                y = results2.loc['male']['expenses'],
                               name = 'male', )

           'layout': mylayout2=go.Layout(title = 'Insurance rate by gender and DC areas',
                                 xaxis= dict(title='Areas in D.C.'),
                                 yaxis= dict(title='Insurance rates')
                                 ),
            go.Figure(data=[mydata2,mydata3],layout=mylayout2)
       }
   )
   ]),
