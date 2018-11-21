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


class BrandManager(models.Manager):
    def create_brand(self, biography, email, gender, name, pic_url, username, business_category, business_city, business_email):
        brand = self.create(biography=biography, email=email, gender=gender, name=name, profile_pic_url=pic_url,
                            username=username, business_category=business_category, business_city=business_city,
                            business_email=business_email)
        brand.save()


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
    objects = BrandManager()


class UserMediaManager(models.Manager):
    def create_user_media(self, user, caption, location):
        user_media = self.create(user=user, caption=caption, location=location)
        user_media.save()


class UserMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=800)
    location = models.CharField(max_length=300)
    objects = UserMediaManager()


class BrandMediaManager(models.Manager):
    def create_brand_media(self, brand, caption, location):
        brand_media = self.create(brand=brand, caption=caption, location=location)
        brand_media.save()


class BrandMedia(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    caption = models.CharField(max_length=800)
    location = models.CharField(max_length=300)
    objects = BrandMediaManager()


class UserCommentManager(models.Manager):
    def create_user_comment(self, user, comment, commented_on):
        user_comment = self.create(user=user, comment=comment, commented_on=commented_on)
        user_comment.save()


class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=800)
    commented_on = models.CharField(max_length=80)
    objects = UserCommentManager()


class BrandCommentManager(models.Manager):
    def create_brand_comment(self, brand, comment, commented_on):
        brand_comment = self.create(brand=brand, comment=comment, commented_on=commented_on)
        brand_comment.save()


class BrandComment(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    comment = models.CharField(max_length=800)
    commented_on = models.CharField(max_length=80)
    objects = BrandCommentManager()
