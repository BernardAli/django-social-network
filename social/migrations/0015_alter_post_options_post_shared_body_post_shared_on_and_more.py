# Generated by Django 4.1.1 on 2022-09-20 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("social", "0014_image_remove_post_image_post_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_on", "-shared_on"]},
        ),
        migrations.AddField(
            model_name="post",
            name="shared_body",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="shared_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="shared_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
