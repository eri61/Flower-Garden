from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World and YAhhhhh.")

# from django.shortcuts import render


# # 以下を追加
# def index (request):
#     return render(request,'hello_world/index.html')
