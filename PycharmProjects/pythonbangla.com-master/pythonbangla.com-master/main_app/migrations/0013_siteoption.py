# Generated by Django 2.0.5 on 2018-05-09 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20180508_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
