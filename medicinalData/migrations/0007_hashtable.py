# Generated by Django 3.0.2 on 2020-01-31 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicinalData', '0006_auto_20200131_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='hashtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashcode', models.CharField(max_length=200)),
                ('pres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicinalData.Prescription')),
            ],
        ),
    ]
