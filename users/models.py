from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image

# Profiles 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_img')

    def __str__(self):
        return f'{self.user.username} Data'

    # Profile Image sizing and saving
    def save(self):
        super().save()

        user_img = Image.open(self.image.path)

        if user_img.width >= 351 or user_img.height >= 351:
            output_size = (350, 350)
            user_img.thumbnail(output_size)
            user_img.save(self.image.path)



# Signal for User/Profile
@receiver(post_save, sender=User)
def register_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()