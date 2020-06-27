from django.urls import path, re_path
from CardManage import views

# app_name = 'CardManage'

urlpatterns = [
    path('addbook/', views.addbook, name="addbook"),
    path('books/', views.books, name="books"),
    re_path(r'(?P<id>\d+)/delete/', views.delbook, name="delbook"),  # ?P<名称>——有名分组，可防止传参混乱
    re_path(r'(?P<id>\d+)/edit/', views.editbook, name="editbook")

]