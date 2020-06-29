from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from CardManage.models import Book
import time

# Create by Hupoz on 2020-06-23.

# 登录页面的视图函数
def login(request):

    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        # print(request.POST)
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_Ajax = request.POST.get("user_Ajax")
        pwd_Ajax = request.POST.get("pwd_Ajax")
        res = {"user_Ajax": None,
               "msg": None}
        print(user_Ajax, pwd_Ajax)

        if user == "zyh" and pwd == "123":
            return HttpResponse("<h2>OK</h2>")
        elif user_Ajax == "zyh" and pwd_Ajax == "123":
            import json
            return HttpResponse(json.dumps(res))
        else:
            return HttpResponse("用户名或密码错误")


# 首页的视图函数
def index(request):
    print("method：", request.method)  # 打印该次请求方式（GET，POST，PUT等）
    print(request.GET)  # 字典，获取GET请求的参数
    print(request.POST)  # 字典，获取POST请求的参数
    print(request.path)  # 获取该次请求的路径（/index/）



    # 模板语法{{}}渲染变量,{%%}渲染标签
    ctime = time.time()
    i = 10
    j = 10
    l = [11,23]
    info = {"name": "yuan", "age": 22}
    b = True
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    zyh = Person('zyh', 23)
    yjx = Person('yjx', 23)

    person_list = [zyh, yjx]



    return render(request, "index.html", locals())  # locals()把变量全部传过去,用.进行深度查询

# 添加书籍的视图函数
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish = request.POST.get('publish')
        date = request.POST.get('pub_date')


        book_obj = Book.objects.create(title=title, price=price, publish=publish, pub_date=date)

        return redirect("/book/books/")

    return render(request, "CardManage/addbook.html")


# 查看全部书籍信息
def books(request):

    book_list = Book.objects.all()  # [obj1, obj2...]
    # message = reverse("book:books")  # 反向解析
    return render(request, "CardManage/books.html", locals())


def delbook(request, id):

    Book.objects.filter(id=id).delete()
    return redirect("/book/books/")


def editbook(request, id):

    book_obj = Book.objects.filter(id=id).first()

    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish = request.POST.get('publish')
        date = request.POST.get('pub_date')

        Book.objects.filter(id=id).update(title=title, price=price, publish=publish, pub_date=date)
        return redirect("/book/books/")


    return render(request, "CardManage/editbook.html", {"book_obj": book_obj})