# Generated by Django 2.2.1 on 2019-06-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no_name', max_length=100, verbose_name='姓名')),
                ('sex', models.CharField(default='male', max_length=50, verbose_name='性别')),
                ('sid', models.CharField(default='0', max_length=100, verbose_name='学号')),
            ],
        ),
    ]
