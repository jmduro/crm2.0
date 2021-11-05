# Generated by Django 3.2.8 on 2021-11-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='contact',
            name='email_opt_out',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='home_phone',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
