# Generated by Django 2.2.5 on 2019-10-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20191008_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp',
            name='description_status',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='description',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placetitle',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placetitle2',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placetitle3',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placetitle4',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placevalue',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placevalue2',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placevalue3',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='placevalue4',
            field=models.CharField(default=' ', max_length=100000),
        ),
    ]
