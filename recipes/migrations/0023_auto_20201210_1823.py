# Generated by Django 3.1.3 on 2020-12-10 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_tag_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('id',), 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterUniqueTogether(
            name='recipefavorite',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='recipeingredient',
            unique_together={('recipe', 'ingredient')},
        ),
    ]