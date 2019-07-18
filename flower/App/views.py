import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.models import Huaban
from App.send import huabanlearn
from dwebsocket.decorators import accept_websocket,require_websocket
import time
from queue import Queue
import threading
from django.urls import reverse
import os
# Create your views here.
# q = Queue(10)
# def load_data():
#
#     return [i for i in range(1,20)]
#
# def htmlproduce(q):
#     index = 0
#     data = load_data()
#     while True:
#         if index < len(data):
#             q.put(data[index])
#             index +=1

@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'ontime.html')
    else:
        while True:
            b = {
                "name": "网站",
                "num": 3,
                "sites": ["Google", "Runoob", "Taobao"]
                }
            a = json.dumps(b)
            # url = q.get()
            for i in range(5):
                # a = bytes(str(b).encode("utf-8"))
                request.websocket.send(a)#发送消息到客户端
                time.sleep(3)
                print("aaaa")


def index(request):
    search = request.POST.get("search")
    if search:
        name = huabanlearn(search)[0]
        print(name)
        huabans = Huaban.objects.filter(name=name)[0:40]
        data = {
            "guojias":huabans
        }

        return render(request, "visit.html",context=data)
    else:
        huabans = Huaban.objects.filter(name="小姐姐")[0:20]
        data = {
            "guojias": huabans
        }
        return render(request,"visit.html",context=data)

# def start(request):
#     print("来了老弟")
#     os.system("cd genera_scrapy;scrapy crawl country")
#     return redirect(reverse("App:index"))
