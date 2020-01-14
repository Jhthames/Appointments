from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['pw_hash']) < 2:
            errors["pw_hash"] = "Password should be at least 2 characters"
        if postData['conf'] != postData['pw_hash']:
            errors["conf"] = "Passwords do not match"   
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):                
            errors['email'] = ("Invalid email address!")
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData['pw_hash']) < 2:
            errors["pw_hash"] = "Password should be at least 2 characters"    
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):                
            errors['email'] = ("Invalid email address!")
        return errors
class AppointmentManager(models.Manager):
    def appointment_validator(self, postData):
        errors = {}
        if len(postData['task']) < 2:
            errors["task"] = "Task should be at least 2 characters"
        # if len(postData['date']) < 2:
        #     errors["date"] = "Date should be entered"
        # if len(postData['status']) < 2:
        #     errors["status"] = "Pending or Done"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Appointment(models.Model):
    task = models.CharField(max_length=255)
    date = models.DateTimeField(max_length=50)
    status = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="appointments", on_delete="CASCADE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AppointmentManager()