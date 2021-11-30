from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField



PROJECT_CATEGORY_CHOICES = (
    ('apps', 'Apps'),
    ('template', 'Template'),
    ('ios', 'IOS'),
    ('ui/ux', 'UI/UX'),
    ('graphic', 'Graphic'),
    ('wireframes','Wireframes')
)


class Service(models.Model):
    image = models.FileField(upload_to="service/")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Catagory(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    user_id = models.AutoField(unique=True, primary_key=True)
    thumbnail = models.ImageField(upload_to="projects/thumbnails/", blank=True, null=True)
    feature_image = models.ImageField(upload_to="projects/feature_image/", blank=True, null=True)
    title = models.CharField(max_length=255)
    is_completed_count = models.BooleanField(default=False)
    is_satisfied_count = models.BooleanField(default=False)
    clients = models.ForeignKey("users.Client",on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


