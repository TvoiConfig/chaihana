# Generated by Django 4.2.6 on 2023-10-10 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('number', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=150, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'Записи',
                'db_table': 'record',
            },
        ),
        migrations.CreateModel(
            name='completedrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_work', models.TextField(default='', verbose_name='Назначенное время и доп. условия')),
                ('record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.record', verbose_name='Выберите клиента')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи Выполненые',
                'db_table': 'completedrecord',
            },
        ),
    ]
