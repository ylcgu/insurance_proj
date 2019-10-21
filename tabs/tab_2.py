import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

filename = 'insurance.csv'
sourceurl = 'http://www.sci.csueastbay.edu/~esuess/stat6620/#week-6'
df = pd.read_csv(filename)

tab_2_layout = html.Div(children=[
    html.H3('Get a life insurance quote today!'),
    html.Div([
            html.H6('Age'),
            dcc.Slider(
                id='slider-1',
                min=18,
                max=80,
                step=1,
                marks={i:str(i) for i in range(18,80)},
                value=30,
            ),
            html.Br(),
            html.H6('Children'),
                dcc.Dropdown(
           id = 'k-drop',
           options=[{'label':0, 'value':0},
                    {'label':1, 'value':1},
                   {'label':2, 'value':2},
                   {'label':3, 'value':3},
                   {'label':4, 'value':4},
                   {'label':5, 'value':5},
                     ],
                  value=0
                  ),
                  html.Br(),
                  html.H6('BMI'),
                  dcc.Slider(
                      id='slider-2',
                      min=10,
                      max=80,
                      step=1,
                      marks={i:str(i) for i in range(10,80)},
                      value=20,
                  ),
                  html.Br(),
                  html.H6('Sex'),
                  dcc.Dropdown(
                       id = 'k-drop-2',
                       options=[{'label':'female', 'value':0},
                                {'label':'male', 'value':1},
                                 ],
                       value=0,
                    ),
                  html.Br(),
                  html.H6('Smoking'),
                  dcc.Dropdown(
                       id = 'k-drop-3',
                       options=[{'label':'smoker', 'value':0},
                                {'label':'non-smoker', 'value':1},
                                 ],
                        value=0
                    ),
                  ]),
                  html.Div([
                          html.Div(id='user-inputs-box', style={'text-align':'center','fontSize':18}),
                          html.Div(id='final_prediction', style={'color':'red','text-align':'center','fontSize':18})
                      ],className='twelve columns'),

])
