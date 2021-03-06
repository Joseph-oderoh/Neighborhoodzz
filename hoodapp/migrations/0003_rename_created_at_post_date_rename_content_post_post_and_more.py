# Generated by Django 4.0.4 on 2022-06-19 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_neighbourhood_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='business',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='neighbourhood',
        ),
        migrations.AddField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='hoodapp.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hoodapp.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='hoodapp.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='hoodapp.profile'),
        ),
    ]
