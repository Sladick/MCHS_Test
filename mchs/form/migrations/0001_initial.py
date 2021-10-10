# Generated by Django 3.2.8 on 2021-10-09 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('limitations', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanRemoval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.FileField(blank=True, upload_to='video/%Y/%m/%d/', verbose_name='План утсранения недостатков')),
                ('number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='form.test')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('patronymic', models.CharField(max_length=55)),
                ('test_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='form.test')),
            ],
        ),
    ]
