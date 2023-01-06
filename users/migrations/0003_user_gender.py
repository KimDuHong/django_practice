# Generated by Django 4.1.4 on 2023-01-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_is_business_user_name_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")],
                default="female",
                max_length=20,
            ),
        ),
    ]