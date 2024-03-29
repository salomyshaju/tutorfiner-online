# Generated by Django 4.0.4 on 2022-10-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Surname', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=250)),
                ('Comment', models.TextField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.TextField(default='')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
