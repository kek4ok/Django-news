# Generated by Django 4.0.6 on 2022-07-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contetnt', models.TextField(blank=True)),
                ('ctreated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
