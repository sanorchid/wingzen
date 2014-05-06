#coding=utf-8

from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

def create_user_detail(sender, instance, signal, *args, **kwargs):
	from .models import Staff
	if kwargs['created']:
		u=Staff()
		u.__dict__.update(instance.__dict__)
		u.save()

post_save.connect(create_user_detail, sender=AbstractUser)