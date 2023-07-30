import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pickle
from tabs import tab_1, tab_2

app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions'] = True
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
app.title = 'Life insurance quote'

app.layout = html.Div([
    html.H1('Life Insurance Quote'),
    dcc.Tabs(id="tabs-template", value='tab-1-template', children=[
        dcc.Tab(label='Data visualization', value='tab-1-template'),
        dcc.Tab(label='Rates quote', value='tab-2-template'),
    ]),
    html.Div(id='tabs-content-template'),
    html.A('View code on github', href='https://github.com/ylcgu/insurance_proj'),
])

@app.callback(Output('tabs-content-template', 'children'),
              [Input('tabs-template', 'value')])
def render_content(tab):
    if tab == 'tab-1-template':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-template':
        return tab_2.tab_2_layout

if __name__ == '__main__':
    app.run_server(debug=True)
