# Generated by Django 3.2.8 on 2021-11-05 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0005_alter_contact_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0002_company_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_name', models.CharField(max_length=50, unique=True)),
                ('amount', models.FloatField(default=0)),
                ('closing_date', models.DateField()),
                ('description', models.TextField(blank=True, max_length=250)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('contact_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
