from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=70)
    username = models.CharField(max_length=80, unique=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=6)
    email = models.EmailField(max_length=254, unique=True)
    country = models.CharField(max_length=75)
    city = models.CharField(max_length=189)


class BrandCategory(models.Model):
    category = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(BrandCategory, on_delete=models.CASCADE)


class Location(models.Model):
    continent = models.CharField(max_length=20)
    country = models.CharField(max_length=75)


class BrandLocation(models.Model):
    brand = models.ForeignKey(Brand, related_name='located_in', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='has_brand', on_delete=models.CASCADE)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    date_created = models.DateTimeField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)


class Hashtag(models.Model):    hashtag = models.CharField(max_length=70)


class HashtagComment(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class HashtagPost(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Emoji(models.Model):
    codes = models.CharField(max_length=50)
    char = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)


class EmojiComment(models.Model):
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class EmojiPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)


class UserFollowing(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followed_by', on_delete=models.CASCADE)
