# Generated by Django 4.2 on 2024-01-14 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month_cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='costs', to=settings.AUTH_USER_MODEL)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='month_costs', to='main.month_cost')),
            ],
        ),
    ]