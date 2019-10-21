import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle
from tabs import tab_1, tab_2

# filename = 'insurance.csv'
# sourceurl = 'http://www.sci.csueastbay.edu/~esuess/stat6620/#week-6'
# df = pd.read_csv(filename)

########### Initiate the app
app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions'] = True
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
app.title='Life insurance quote'

## Layout
app.layout = html.Div([
    html.H1('Life Insuarance Quote'),
    dcc.Tabs(id="tabs-template", value='tab-1-template', children=[
        dcc.Tab(label='Data visualization', value='tab-1-template'),
        dcc.Tab(label='Rates quote', value='tab-2-template'),
    ]),
    html.Div(id='tabs-content-template')
])


############ Callbacks

@app.callback(Output('tabs-content-template', 'children'),
              [Input('tabs-template', 'value')])
def render_content(tab):
    if tab == 'tab-1-template':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-template':
        return tab_2.tab_2_layout

# Tab 1 callbacks


########### tab2 layout
# app.layout = html.Div(children=[
#     html.H1('Get a life insurance quote today!'),
#     html.Div(['choose your information']),
#     html.Div([
#             html.H6('Age'),
#             dcc.Slider(
#                 id='slider-1',
#                 min=18,
#                 max=80,
#                 step=1,
#                 marks={i:str(i) for i in range(18,80)},
#                 value=30,
#             ),
#             html.Br(),
#             html.H6('Children'),
#                 dcc.Dropdown(
#            id = 'k-drop',
#            options=[{'label':0, 'value':0},
#                     {'label':1, 'value':1},
#                    {'label':2, 'value':2},
#                    {'label':3, 'value':3},
#                    {'label':4, 'value':4},
#                    {'label':5, 'value':5},
#                      ],
#                   value=0
#                   ),
#                   html.Br(),
#                   html.H6('BMI'),
#                   dcc.Slider(
#                       id='slider-2',
#                       min=10,
#                       max=80,
#                       step=1,
#                       marks={i:str(i) for i in range(10,80)},
#                       value=20,
#                   ),
#                   html.Br(),
#                   html.H6('Sex'),
#                   dcc.Dropdown(
#                        id = 'k-drop-2',
#                        options=[{'label':'female', 'value':0},
#                                 {'label':'male', 'value':1},
#                                  ],
#                        value=0,
#                     ),
#                   html.Br(),
#                   html.H6('Smoking'),
#                   dcc.Dropdown(
#                        id = 'k-drop-3',
#                        options=[{'label':'smoker', 'value':0},
#                                 {'label':'non-smoker', 'value':1},
#                                  ],
#                         value=0
#                         ),
#            html.Br(),
#               #html.H6('STOCK MARKET TICKERS'),
#               html.H6(
#               children = 'try some graph',
#               ),
#               # dcc.Graph(
#               #     id='volume',
#               #     figure={
#               #         'data': [
#               #             go.Bar(x = results2.loc['female'].index,
#               #                              y = results2.loc['female']['expenses'],
#               #                              name = 'female',
#               #                              ),
#               #             go.Bar(x = results2.loc['male'].index,
#               #                   y = results2.loc['male']['expenses'],
#               #                   name = 'male', )
#               #           ],
#               #           'layout': go.Layout(title = 'Insurance rate by gender and DC areas',
#               #                               xaxis= dict(title='Areas in D.C.'),
#               #                               yaxis= dict(title='Insurance rates')
#               #                               )
#               #           }
#               # )
#               # ]),
#     html.Div(id='output-message', children=''),
#     html.Br(),
#     html.A('Code on Github', href='https://github.com/ylcgu/insurance_proj/'),
# ])


# Tab 2 Callback # 1
@app.callback(Output('user-inputs-box', 'children'),
            [
              Input('slider-1', 'value'),
              Input('k-drop', 'value'),
              Input('slider-2', 'value'),
              Input('k-drop-2', 'value'),
              Input('k-drop3', 'value'),

              ])
def update_user_table(family, age, cabin, title, sex, embark):
    return html.Div([
        html.Div(f'slider-1: {age}'),
        html.Div(f'k-drop: {children}'),
        html.Div(f'slider-2: {bmi}'),
        html.Div(f'k-drop-2: {sex}'),
        html.Div(f'k-drop3: {smoker}'),
    ])

# Tab 4 callback 2
@app.callback(Output('final_prediction','children'),
              [
               Input('slider-1', 'value'),
               Input('slider-2', 'value'),
               Input('k-drop', 'value'),
               Input('k-drop-2','value'),
               Input('k-drop-3','value')
               ])
def my_funcky_function(value0,value1,k1,k2,k3):
    # read in the chosen model
    file = open('final_model.pkl', 'rb')
    model = pickle.load(file)
    file.close()
# define the new observation
    new_obs=[[value0,value1,k1,k2,k3]]
    my_prediction = model.predict(new_obs)
    return f'Your quote is : ${my_prediction}'
    # return 'this is a test'
############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
