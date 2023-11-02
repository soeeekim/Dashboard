import plotly.express as px
from dash import dcc, html

import pandas as pd
import plotly.graph_objects as go
import dash

data1 = pd.read_csv("결과.csv", encoding="cp949")  # 첫 번째 데이터 파일
data2 = pd.read_csv("결과2.csv", encoding="cp949")  # 두 번째 데이터 파일
data3 = pd.read_csv("결과3.csv", encoding="cp949") 
data4 = pd.read_csv("결과4.csv", encoding="cp949") 

# 데이터 프레임 조작 작업
data1 = data1.loc[:, ["Result1", "Number1"]]
data1.columns = ["Result", "Number"]
data2 = data2.loc[:, ["Result2", "Number2"]]
data2.columns = ["Result", "Number"]
data3 = data3.loc[:, ["Result3", "Number3"]]
data3.columns = ["Result", "Number"]
data4 = data4.loc[:, ["Result4", "Number4"]]
data4.columns = ["Result", "Number"]

fig1 = go.Figure(data=[go.Pie(labels=data1["Result"], values=data1["Number"])])
fig1.update_layout(title="Integration Test 결과")

fig2 = go.Figure(data=[go.Pie(labels=data2["Result"], values=data2["Number"])])
fig2.update_layout(title="System Test 결과")

fig3 = go.Figure(data=[go.Pie(labels=data3["Result"], values=data3["Number"])])
fig3.update_layout(title="Log Test 결과")

fig4 = go.Figure(data=[go.Pie(labels=data4["Result"], values=data4["Number"])])
fig4.update_layout(title="Installation & Upgrade Test 결과")

app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(
        children="Test 결과",
        style={"textAlign": "center"}
    ),
    html.H4(
        children="Pass/Fail율",
    ),
    html.Div([
        html.Div(dcc.Graph(id="graph1", figure=fig1), className="six columns"),
        html.Div(dcc.Graph(id="graph2", figure=fig2), className="six columns"),
    ], className="row"),
    html.Div([
        html.Div(dcc.Graph(id="graph3", figure=fig3), className="six columns"),
        html.Div(dcc.Graph(id="graph4", figure=fig4), className="six columns"),
    ], className="row"),
], style={"width": "90%", "margin": "auto"})


if __name__ == '__main__':
    app.run_server(debug=True)



