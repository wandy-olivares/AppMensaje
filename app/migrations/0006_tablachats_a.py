# Generated by Django 4.1.7 on 2023-04-06 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_amigos_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablachats',
            name='a',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.amigos'),
        ),
    ]