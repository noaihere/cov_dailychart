import pandas as pd
import plotly.express as px
df=pd.read_csv('https://raw.githubusercontent.com/noaihere/cov_dailychart/master/total_df.csv')
df_com=pd.read_csv('https://raw.githubusercontent.com/noaihere/cov_dailychart/master/com_df.csv')
t=df.merge(df_com, on='metric', how='left')
t['value']=t.apply(lambda x: x["value_y"] if pd.notnull(x["value_y"]) else x["value_x"], axis=1)

t = t.loc[t.category_1=='additional',:]
t= t[['metric', 'category_2','value']]
fig = px.sunburst(t, path=['metric', 'category_2'], values='value',color='metric', color_discrete_map={'community':'gold'})
fig.update_layout(uniformtext_minsize=52, 
    margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor="LightSteelBlue",
)


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1("daily charts"),
    dcc.Graph(
        id='flyingdog',
        figure=fig
    )])

if __name__ == '__main__':
    app.run_server()
