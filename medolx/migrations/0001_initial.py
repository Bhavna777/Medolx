# Generated by Django 3.1.5 on 2021-05-07 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('desc', models.CharField(max_length=300)),
                ('featured_pic', models.ImageField(blank=True, null=True, upload_to='blog_pic/BlogFeaturedPic/')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('author_pic', models.ImageField(blank=True, null=True, upload_to='blog_pic/BlogAuthorPic/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=35)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/ProductProfilePic/')),
                ('used_for', models.CharField(max_length=40)),
                ('rate', models.CharField(max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('cpassword', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=35)),
                ('phone_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=40)),
                ('qualification', models.CharField(max_length=25)),
                ('hospital_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50)),
                ('consultation_fee', models.CharField(max_length=5)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/')),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
