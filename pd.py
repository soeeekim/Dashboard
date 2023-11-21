import plotly.express as px #그래프 구성요소로 데이터를 넣어서 graph object로 반환하는 방식
import pandas as pd #조작 및 분석 처리
import plotly.graph_objects as go #인터랙티브 시각화 #그래프 구성요소를 객체마다 작성하여 그래프를 작성하는 방식
import dash #웹 프레임워크 처리
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import numpy as np #행렬 및 배열 처리
from plotly.colors import DEFAULT_PLOTLY_COLORS #플러티 기본 색상 값
from selenium import webdriver #webdriver 클래스는 브라우저별 클래스 변수를 생성하여 드라이버와 연결해주는 역학
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager #드라이버의 자동설치를 위한 라이브러리 불러옴
from selenium.webdriver.common.keys import Keys #키입력을 위한 라이브러리 불러옴 > Return
from selenium.webdriver.common.by import By #By클래스는 웹 사이트에서 원하는 요소 가리킬때사용하는 클래스
import requests
from lxml import etree

# Jira 인스턴스 URL 및 인증 정보
url = 'https://hutomdev.atlassian.net/rest/api/2/search'
username = 'sohee.kim@hutom.co.kr'
api_token = 'ATATT3xFfGF0DwKPMR70ciElrdet3UN55fEHlUx9UKTtak4LhgBuwuyssyi3eyqHmJ-twf_vMWoH2eF3qmhbLZRalTLTKTB23d3S9TX9c1-6Y1JoTgPtXzD7Tu42JlyqGqagUerjHhQrUefmXJBJkGf8l3o8xOSh6wRcRx4w-NCP1xNQj7oEYHA=F1A61419'
project_key = 'HS'
release_version = '24225'


#해야 할 일 이슈 갯수 가져오기
jql_1 = f'project = {project_key} AND status = "To Do" AND parent = 24255'

response_1 = requests.get(
    url,
    auth=(username, api_token),
    params={'jql': jql_1, 'maxResults': 0, 'startAt': 0, 'fields': 'total'}
)

if response_1.status_code == 200:
    data = response_1.json()
    total_issues1 = data['total']
    print(f"Total issues in '해야 할 일' status: {total_issues1}")
else:
    print(f"Failed to retrieve data. Status code: {response_1.status_code}")

#In-Progress 이슈 갯수 가져오기
jql_2 = f'project = {project_key} AND status = "In Progress" AND parent = 24255 '

response_2 = requests.get(
    url,
    auth=(username, api_token),
    params={'jql': jql_2, 'maxResults': 0, 'startAt': 0, 'fields': 'total'}
)

if response_2.status_code == 200:
    data = response_2.json()
    total_issues2 = data['total']
    print(f"Total issues in '진행 중' status: {total_issues2}")
else:
    print(f"Failed to retrieve data. Status code: {response_2.status_code}")


#개발자 수정 완료 이슈 갯수 가져오기
jql_dev = f'project = {project_key} AND status = "개발자 수정 완료" AND parent = 24255'

response_dev = requests.get(
    url,
    auth=(username, api_token),
    params={'jql': jql_dev, 'maxResults': 0, 'startAt': 0, 'fields': 'total'}
)

if response_dev.status_code == 200:
    data = response_dev.json()
    total_issues4 = data['total']
    print(f"Total issues in '개발자 수정 완료' status: {total_issues4}")
else:
    print(f"Failed to retrieve data. Status code: {response_dev.status_code}")

#검증 완료 이슈 갯수 가져오기
jql_verify = f'project = {project_key} AND status = "검증완료" AND parent = 24255 '

response_verify = requests.get(
    url,
    auth=(username, api_token),
    params={'jql': jql_verify, 'maxResults': 0, 'startAt': 0, 'fields': 'total'})
            
if response_verify .status_code == 200:
    data = response_verify.json()
    total_issues5 = data['total']
    print(f"Total issues in '검증완료' status: {total_issues5}")
else:
    print(f"Failed to retrieve data. Status code: {response_verify .status_code}")            

#app정의
app = dash.Dash(__name__) 
#웹브라우저 탭 타이틀
app.title= ("[ 검증 현황 Dashboard ]") 
#server 정의
server = app.server  

#excel 파일 읽어오기
data1 = pd.read_csv("결과.csv", encoding="cp949")  
data2 = pd.read_csv("결과2.csv", encoding="cp949")  
data3 = pd.read_csv("결과3.csv", encoding="cp949") 
data4 = pd.read_csv("결과4.csv", encoding="cp949") 
data5 = pd.read_csv("결과5.csv", encoding="cp949") 

# 데이터 프레임 조작 작업
data1 = data1.loc[:, ["Result1", "Number1"]]
data1.columns = ["Result", "Number"]
data2 = data2.loc[:, ["Result2", "Number2"]]
data2.columns = ["Result", "Number"]
data3 = data3.loc[:, ["Result3", "Number3"]]
data3.columns = ["Result", "Number"]
data4 = data4.loc[:, ["Result4", "Number4"]]
data4.columns = ["Result", "Number"]
data5 = data5.loc[:, ["Result4", "Number4"]]
data5.columns = ["Result", "Number"]

#첫번쨰 Pie 그래프 data, layout 정하기 
trace0 = go.Pie(labels=data4["Result"],values=data4["Number"])
data=[trace0]
layout=go.Layout()
fig0=go.Figure(data, layout)

#두번쨰 Pie 그래프 data, layout 정하기 
trace1 = go.Pie(labels=data1["Result"],values=data1["Number"])
data=[trace1]
layout=go.Layout(title="Integration Test 결과")
fig1=go.Figure(data, layout)

#세번쨰 Pie 그래프 data, layout 정하기 
trace2 = go.Pie(labels=data2["Result"],values=data2["Number"])
data=[trace2]
layout=go.Layout(title="System Test 결과")
fig2=go.Figure(data, layout)

#네번쨰 Pie 그래프 data, layout 정하기 
trace3 = go.Pie(labels=data3["Result"],values=data3["Number"])
data=[trace3]
layout=go.Layout(title="Log Test 결과")
fig3=go.Figure(data, layout)

#다섯번쨰 Pie 그래프 data, layout 정하기 
trace6 = go.Pie(labels=data5["Result"],values=data5["Number"])
data=[trace6]
layout=go.Layout(title="Upgrade&Install Test 결과")
fig6=go.Figure(data, layout)

#Bar 그래프 Data set 
issue_statuses = ['To Do', 'In Progress', '개발자 수정 완료', '검증완료']
issue_counts = [total_issues1, total_issues2, total_issues4, total_issues5]
#Bar 그래프 data, layout 정하기 
trace4 = go.Bar(x= issue_statuses, y=issue_counts)
data=[trace4]
layout=go.Layout(title="Status별 이슈 수")
fig4=go.Figure(data, layout)

#메모 이슈 타이틀 가져오기
jql_4 = f'project = {project_key} AND parent = 24255'

response_4 = requests.get(
    url,
    auth=(username, api_token),
    params={'jql': jql_4, 'maxResults': 100, 'startAt': 0, 'fields': 'summary'}
)

data = response_4.json()

# 메모 표시
issue_titles=[]
issues = data['issues']
for issue in issues:
    issue_title = issue['fields']['summary']
    print("이슈 제목:", issue_title)
    issue_titles.append(issue_title)

memo = ''
for title in issue_titles:
    memo += f"- {title}\n\n"


#layout 정의
app.layout = html.Div([
    #title 정의
    html.H2('검증 현황 Dashboard', style={'textAlign': 'center', 'marginBottom': 10, 'marginTop': 50, 'marginLeft': 100, 'marginRight': 100}),
    #영역 나누기 -left
    html.Div([
        
        html.Div(className='Pie', children=[
            html.H3('전체 Test 진행 상황 (WBS기준)', style={'textAlign': 'center', 'marginBottom': '20px', 'marginTop': '30px'}),
            html.Div(dcc.Graph(id='all', figure=fig0), style={ 'marginLeft': 50, 'marginRight': 50}),
            html.H3('각 Test 결과', style={'textAlign': 'center', 'marginBottom': '50px', 'marginTop': '50px'}),
            html.Div(dcc.Graph(id='Integration Test', figure=fig1), style={'float': 'right', 'display': 'inline-block', 'width': '50%'}),
            html.Div(dcc.Graph(id='System Test', figure=fig2), style={'float': 'left', 'display': 'inline-block', 'width': '50%'}),
            html.Div(dcc.Graph(id='Log Test', figure=fig3), style={'float': 'right', 'display': 'inline-block', 'width': '50%'}),
            html.Div(dcc.Graph(id='Upgrade&Install Test', figure=fig6), style={'float': 'left', 'display': 'inline-block', 'width': '50%'})
        ]),
    ], style={'float': 'left', 'width': '50%'}),

    #영역 나누기 -right
    html.Div([
        html.H3('Jira 이슈 상황', style={'textAlign': 'center', 'marginBottom': '30px', 'marginTop': '30px'}),
        html.Div(html.Div(dcc.Graph(id='jira', figure=fig4))),
        html.Div([html.H4('현 버전에서 생성된 이슈'),
        html.Pre(memo)
        ], style={'margin': '30px', 'padding': '10px', 'border': '1px solid #ccc', 'marginLeft': 50, 'marginRight': 50})
        ], style={'float': 'right', 'width': '50%'})

])


if __name__ == '__main__':
    app.run_server(debug=True)


