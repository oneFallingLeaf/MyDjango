from django.db import models

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length=16,blank=False,null=False)
    password = models.CharField(max_length=16,blank=False,null=False)
    full_name = models.CharField(max_length=16,blank=False,null=False)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)
    auth_type = models.IntegerField()
    # jobs = models.ForeignKey(Job)
    def __str__(self):
        return self.user_name



# class Job(models.Model):
#     ticket_number = models.CharField(max_length=12)
