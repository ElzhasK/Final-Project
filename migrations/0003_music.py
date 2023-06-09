# Generated by Django 4.1.6 on 2023-05-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizcategory_quizquestion_submittedanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('music_file', models.FileField(upload_to='music/')),
            ],
        ),
    ]
