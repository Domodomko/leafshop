# Generated by Django 4.1.1 on 2022-09-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='about_tea_en',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='about_tea_ru',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='black_tea_en',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='black_tea_ru',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='camelia_en',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='camelia_ru',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='green_tea_en',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='green_tea_ru',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='names_of_tea_en',
        ),
        migrations.RemoveField(
            model_name='aboutteacontent',
            name='names_of_tea_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='privacy_policy_en',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='privacy_policy_ru',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='return_policy_en',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='return_policy_ru',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='shipping_policy_en',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='shipping_policy_ru',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='term_of_service_en',
        ),
        migrations.RemoveField(
            model_name='shoppolicy',
            name='term_of_service_ru',
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_province',
            field=models.CharField(choices=[('Batken', 'Batken'), ('Jalalabat', 'Jalalabat'), ('Issykkul', 'Issykkul'), ('Osh', 'Osh'), ('Talas', 'Talas'), ('Chui', 'Chui'), ('Naryn', 'Naryn')], default='', max_length=50, null=True, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_province',
            field=models.CharField(choices=[('Batken', 'Batken'), ('Jalalabat', 'Jalalabat'), ('Issykkul', 'Issykkul'), ('Osh', 'Osh'), ('Talas', 'Talas'), ('Chui', 'Chui'), ('Naryn', 'Naryn')], max_length=50, null=True, verbose_name='Province'),
        ),
    ]