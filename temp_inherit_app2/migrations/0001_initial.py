# Generated by Django 5.1.4 on 2025-01-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newuser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Teach_name', models.CharField(max_length=20)),
                ('stu_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=4)),
            ],
        ),
    ]
