from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=500)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_image = models.ImageField(default='default_post_image.jpg', upload_to='post_pics')
	search_fields = ('title', 'subtitle', 'content')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Lifestyle_post(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=500)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_image = models.ImageField(default='default_post_image.jpg', upload_to='post_pics')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})