from django.db import models
from django.contrib.auth.models import User


# Create your models here.
'''class club(models.Model) :
    email=models.EmailField()
    password=models.CharField(max_length=20)'''
class clubevents(models.Model) :
    cname=models.CharField(max_length=30)
    cemail=models.CharField(max_length=30)
    ename=models.CharField(max_length=100)
    edate=models.CharField(max_length=30)
    evenue=models.CharField(max_length=100)
    etime=models.CharField(max_length=20)
    etype=models.CharField(max_length=20)
    edesc=models.CharField(max_length=400)
    eligibility=models.CharField(max_length=30)
    elink=models.CharField(max_length=400)
    efee=models.CharField(max_length=400)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user.username
