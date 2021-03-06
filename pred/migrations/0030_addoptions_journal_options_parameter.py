# Generated by Django 3.0.3 on 2020-04-14 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0029_auto_20200409_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_option', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journl_name', models.CharField(max_length=200)),
                ('journal_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=100)),
                ('journal', models.ManyToManyField(to='pred.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
                ('new_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pred.AddOptions')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pred.Parameter')),
            ],
        ),
    ]
