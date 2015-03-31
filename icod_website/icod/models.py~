from django.db import models

# Create your models here.
class TeamMember(models.Model):
	name = models.CharField(max_length=128)
	picture = models.ImageField(upload_to='teamPhotos', blank=True)
	jobTitle = models.CharField(max_length=128)
	about = models.TextField(max_length=1000)

	def __unicode__(self):
		return self.name

class Home(models.Model):
	intro = models.TextField(max_length=1000)

	def __unicode__(self):
		return 'Introduction'

class Category(models.Model):
	name = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name

class NewsItem(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=300)
	date = models.DateField(auto_now=True, auto_now_add=False)
	news = models.TextField(max_length=1000)

	def __unicode__(self):
		return self.title
