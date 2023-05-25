from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from PIL import Image


# Profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='v1684659602/media/profile_img/default_kpyvr1')
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Data'

    # Profile Image sizing and saving
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if isinstance(self.image, str):
            try:
                user_img = Image.open(self.image)

                if user_img.width >= 351 or user_img.height >= 351:
                    output_size = (350, 350)
                    user_img.thumbnail(output_size)
                    user_img.save(self.image)
            except FileNotFoundError:
                pass
        elif isinstance(self.image, CloudinaryField):
            try:
                user_img = Image.open(self.image.url)

                if user_img.width >= 351 or user_img.height >= 351:
                    output_size = (350, 350)
                    user_img.thumbnail(output_size)
                    user_img.save(self.image.path)
            except FileNotFoundError:
                pass

    # Delete User profile            
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


# Signals for User/Profile
@receiver(post_save, sender=User)
def register_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()