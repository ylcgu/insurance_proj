import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd

########### Define your variables ######
#
# ########### Set up the data
df = pd.read_csv('insurance.csv')
#
result1= df.groupby(['sex'])['expenses'].mean().sort_values(ascending=False)

mydata = go.Bar(
        x =result1.index,
        y= result1.values,
        marker={'color': ['yellow', 'red']})
mylayout = go.Layout(
        title ='Insurance rates by gender',
        xaxis= dict(title='gender'),
        yaxis= dict(title='insurance rates'))
myfigure = go.Figure([mydata],mylayout)
myfigure


results2= df.groupby(["sex", "smoker"])["expenses"].mean().sort_values(ascending=False)
results2 = pd.DataFrame(results2)
results2
#
#
mydata2 = go.Bar(x = results2.loc['female'].index,
                 y = results2.loc['female']['expenses'],
                 name = 'female', )
mydata3 = go.Bar(x = results2.loc['male'].index,
                  y = results2.loc['male']['expenses'],
                 name = 'male', )
# mydata4 = go.Bar(x = results2.loc['Shared room'].index,
#                   y = results2.loc['Shared room']['room'],
#                  name = 'Shared room', )
mylayout2 = go.Layout(title = 'Smokers of the insurance rate by gender',
                      xaxis= dict(title='Areas in D.C.'),
                      yaxis= dict(title='Insurance rates')
                      )
#
myfigure2=go.Figure(data=[mydata2,mydata3],layout=mylayout2)
myfigure2

########### Initiate the app
# app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
# server = app.server
# app.title='Data visualization'

########### Set up the layout
tab_1_layout = html.Div(children=[
    dcc.Graph(
        id='figure-1',
        figure=myfigure
     ),
    dcc.Graph(
        id='figure-2',
        figure=myfigure2
    ),
    ]
)
