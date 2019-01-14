import MySQLdb
from django.http import HttpResponse
from django.shortcuts import render
from pyecharts import Bar
# Create your views here.

conn = MySQLdb.Connect(
            host='127.0.0.1',
            port=3306,
            db='bingdong',
            user='root',
            password='562676',
            charset='utf8'
        )
cursor = conn.cursor()
sql = 'select city,num from t_city'
cursor.execute(sql)
datas=cursor.fetchall()#530北京 538上海 763广州 765深圳
# print(datas)

# datas=(('530', '453399'), ('538', '307284'), ('763', '222639'), ('765', '246831'))
l=[]
city=[]
num=[]
for data in datas:
    if data[0]=='530':
        l.append(['北京',data[1]])
        city.append('北京')
        num.append(int(data[1]))
    elif data[0]=='538':
        l.append(['上海', data[1]])
        city.append('上海')
        num.append(int(data[1]))
    elif data[0]=='763':
        l.append(['广州', data[1]])
        city.append('广州')
        num.append(int(data[1]))
    elif data[0]=='765':
        l.append(['深圳', data[1]])
        city.append('深圳')
        num.append(int(data[1]))

def demo(request):
    # bar = Bar("城市招聘量", "这里是副标题")
    # bar.use_theme('dark')
    # bar.add("城市", city,num )
    # bar.render('F:demo.html')
    # return HttpResponse()
    pass

def demo1(request):
    pass