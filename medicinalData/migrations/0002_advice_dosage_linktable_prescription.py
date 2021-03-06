# Generated by Django 3.0.2 on 2020-01-30 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicinalData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='linktable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=200)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Prescription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dosage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_day', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('when', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=10)),
                ('med', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Medicine')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv', models.CharField(max_length=200, null=True)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Prescription')),
            ],
        ),
    ]
