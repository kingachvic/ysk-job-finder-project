# Generated by Django 3.1.3 on 2020-12-28 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201216_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='art',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='carwash',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='chips',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='cobler',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='cyber',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='eggs',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='kinyozi',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='kiosk',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='mkokoteni',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='mutura',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='tea',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='water',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Jobnames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinyozi', models.IntegerField(default=0)),
                ('chips', models.IntegerField(default=0)),
                ('kiosk', models.IntegerField(default=0)),
                ('water', models.IntegerField(default=0)),
                ('art', models.IntegerField(default=0)),
                ('carwash', models.IntegerField(default=0)),
                ('cyber', models.IntegerField(default=0)),
                ('mkokoteni', models.IntegerField(default=0)),
                ('tea', models.IntegerField(default=0)),
                ('cobler', models.IntegerField(default=0)),
                ('mutura', models.IntegerField(default=0)),
                ('eggs', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.place')),
            ],
        ),
    ]
