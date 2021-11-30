from django.db import models
from django.db.models.deletion import CASCADE



class Testimonial(models.Model):
    message = models.TextField(default=0)
    clients = models.ForeignKey("users.Client",on_delete=CASCADE,blank=True,null=True)


class Contact(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=255,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
     return self.email
