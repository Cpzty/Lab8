from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    post_text = models.CharField(max_length=200)
    poster = models.ManyToManyField(User,through='PostedBy')
    
class PostedBy(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE )
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE )

class LikedBy(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE )
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE )

