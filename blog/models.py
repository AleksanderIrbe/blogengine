from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def latinizator(letter, dic):
		for i, j in dic.items():
			letter = letter.replace(i, j)
		return letter

def gen_slug(s):
	rus_slug = slugify(s, allow_unicode=True)
	#транслитерация
	legend = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'y','ы':'y','ь':"'",'э':'e','ю':'yu','я':'ya',}
	new_slug = latinizator(rus_slug, legend)
	return new_slug + '-' + str(int(time()))

class Post(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, unique=True, blank=True )
	body = models.TextField(blank=True, db_index=True)
	tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
	date_pub = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('post_detail_url', kwargs={'slug':self.slug})

	def get_update_url(self):
		return reverse('post_update_url', kwargs={'slug':self.slug})
		#return reverse('tag_update_url', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('post_delete_url', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)

	def get_absolute_url(self):
		return reverse('tag_detail_url', kwargs={'slug':self.slug})
#TODO надо ли добавлять автоматизацию создания слага. Надо ли id или проверять уникальность как-то иначе

	def get_update_url(self):
		return reverse('tag_update_url', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('tag_delete_url', kwargs={'slug':self.slug})

	def __str__(self):
		return self.title			
						