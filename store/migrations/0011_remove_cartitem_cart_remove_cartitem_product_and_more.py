# Generated by Django 4.2.2 on 2023-09-18 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_cartitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]