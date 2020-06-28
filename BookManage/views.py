from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from BookManage.models import Book, Publish, Author


# Create by Hupoz on 2020-06-23.


# 查看全部书籍信息
def books(request):
    book_list = Book.objects.all()  # [obj1, obj2...]
    # message = reverse("bookpro:books")  # 反向解析
    return render(request, "BookManage/books.html", locals())


def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish_id')
        date = request.POST.get('pub_date')
        authors_id_list = request.POST.getlist('authors_id_list')  # 针对多选

        book_obj = Book.objects.create(title=title, price=price, pub_date=date, publish_id=publish_id)
        book_obj.authors.add(*authors_id_list)
        return redirect("/bookpro/books/")

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request, "BookManage/addbook.html", {"publish_list": publish_list, "author_list": author_list})


def editbook(request, id):
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    book_obj = Book.objects.filter(id=id).first()

    return render(request, "BookManage/editbook.html", locals())
