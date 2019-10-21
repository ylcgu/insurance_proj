import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd

########### Define your variables ######
myheading = "Insurance rates vary from people "
tabtitle = 'Look at our visualization'
filename = '../insurance.csv'
sourceurl = 'http://www.sci.csueastbay.edu/~esuess/stat6620/#week-6'
githublink = 'https://github.com/ylcgu/insurance_proj'
#
# ########### Set up the data
df = pd.read_csv(filename)
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


results2= df.groupby(["sex", "smoker"])["expenses"].count().sort_values(ascending=False)
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
mylayout2 = go.Layout(title = 'Insurance rate by gender and DC areas',
                      xaxis= dict(title='Areas in D.C.'),
                      yaxis= dict(title='Insurance rates')
                      )
#
myfigure2=go.Figure(data=[mydata2,mydata3],layout=mylayout2)
myfigure2

########### Initiate the app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='Data visualization'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=myfigure
     ),
    dcc.Graph(
        id='figure-2',
        figure=myfigure2
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
