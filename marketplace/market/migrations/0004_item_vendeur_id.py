# Generated by Django 5.0.4 on 2024-04-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_user_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='vendeur_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
