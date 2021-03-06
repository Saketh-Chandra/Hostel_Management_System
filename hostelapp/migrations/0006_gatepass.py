# Generated by Django 3.1.3 on 2021-03-01 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0005_auto_20201218_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='gatepass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateTimeField(auto_created=True)),
                ('outing_data', models.DateField(null=True)),
                ('return_date', models.DateField(null=True)),
                ('count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.student_room')),
            ],
        ),
    ]