# Generated by Django 5.1.6 on 2025-02-14 23:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveBigIntegerField(unique=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('stored_at', models.DateTimeField(auto_now_add=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='provider.provider')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='block.currency')),
            ],
            options={
                'unique_together': {('currency', 'number')},
            },
        ),
    ]
