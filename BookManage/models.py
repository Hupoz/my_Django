from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()


# 出版社表
class Publish(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # 与publish建立一对多的关系，外键字段建立在多的一方，字段尾自动拼接_id
    publish = models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)

    # 与Author建立多对多的关系，外键字段建立在多的一方，生成Book_Authors
    authors = models.ManyToManyField(to="Author")

