# Generated by Django 3.1.5 on 2021-04-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210330_1210'),
        ('advisement', '0016_auto_20210422_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisee',
            name='advisors',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Faculty'),
        ),
        migrations.AlterField(
            model_name='advisee',
            name='id_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
