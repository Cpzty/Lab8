# Generated by Django 2.1.2 on 2018-10-04 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_auto_20181003_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LikedBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Like')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.User')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.ManyToManyField(through='instagram.LikedBy', to='instagram.Post'),
        ),
    ]
