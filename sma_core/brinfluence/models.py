from django.db import models


class UserManager(models.Manager):
    def create_user(self, biography, email, gender, name, pic_url, username, birthdate):
        user = self.create(biography=biography, email=email, gender=gender, name=name, profile_pic_url=pic_url,
                           username=username, date_of_birth=birthdate)
        user.save()


class User(models.Model):
    biography = models.CharField(max_length=350)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=6)
    name = models.CharField(max_length=70)
    profile_pic_url = models.CharField(max_length=300)
    username = models.CharField(max_length=80, unique=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    objects = UserManager()


class Brand(models.Model):
    biography = models.CharField(max_length=350)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=11)
    name = models.CharField(max_length=150)
    profile_pic_url = models.CharField(max_length=300)
    username = models.CharField(max_length=80, unique=True)
    business_category = models.CharField(max_length=80)
    business_city = models.CharField(max_length=70)
    business_email = models.EmailField(max_length=254)


class UserMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=800)
    location = models.CharField(max_length=300)


class BrandMedia(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    caption = models.CharField(max_length=800)
    location = models.CharField(max_length=300)


class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=800)
    commented_on = models.CharField(max_length=80)


class BrandComment(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    comment = models.CharField(max_length=800)
    commented_on = models.CharField(max_length=80)
