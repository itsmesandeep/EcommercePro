from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def uName_Validator(uname):
    if len(uname) < 6:
        raise ValidationError('uName Must be Greater than 6 Char')
    elif len(uname) > 10:
        raise ValidationError('uName Must be Less Than 10 Chars')


class RegistrationsData(models.Model):
    uname = models.CharField(max_length=100, validators=[uName_Validator])
    password = models.CharField(max_length=100)
    mobileNo = models.IntegerField()
    emailId = models.EmailField(max_length=100)
