# Generated by Django 4.0.4 on 2022-10-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_remove_report_user_report_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='CreatedDate',
            field=models.DateField(default=1984),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateField(),
        ),
    ]