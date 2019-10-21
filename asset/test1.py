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
