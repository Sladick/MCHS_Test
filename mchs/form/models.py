from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)
    limitations = models.TextField()

    def __str__(self):
        return self.title


class PlanRemoval(models.Model):
    plan = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='План утсранения недостатков', blank=True)
    number = models.ForeignKey('Test', on_delete=models.CASCADE)


class People(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    patronymic = models.CharField(max_length=55)
    test_number = models.ForeignKey('Test', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
