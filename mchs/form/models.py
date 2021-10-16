from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=155)
    rating = models.FloatField()
    limitations = models.TextField()
    many_plan = models.ManyToManyField('Plan')
    many_people = models.ManyToManyField('People')

    def __str__(self):
        return self.title


class Plan(models.Model):
    file = models.CharField(max_length=100)

    def __str__(self):
        return self.file


class People(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)

    def __str__(self):
        return self.name