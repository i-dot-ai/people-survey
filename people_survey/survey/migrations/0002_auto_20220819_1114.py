# Generated by Django 3.2.13 on 2022-08-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]