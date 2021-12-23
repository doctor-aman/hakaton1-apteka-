# Generated by Django 4.0 on 2021-12-22 15:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='product.groupproduct'),
            preserve_default=False,
        ),
    ]