# Generated by Django 3.2.8 on 2021-10-10 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20211010_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='test_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='form.test'),
        ),
    ]
