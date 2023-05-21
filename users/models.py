from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Profiles 
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from PIL import Image
from urllib.request import urlopen
from io import BytesIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='https://res.cloudinary.com/dmbdqco85/image/upload/v1684529632/profile_img/nomad1_iztuvi.jpg', upload_to='profile_img', storage=RawMediaCloudinaryStorage())
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Data'

    def save(self, *args, **kwargs):
        if self.image.url == 'https://res.cloudinary.com/dmbdqco85/image/upload/v1684529632/profile_img/nomad1_iztuvi.jpg':
            # Skip resizing and saving if the default image is used
            super().save(*args, **kwargs)
            return

        super().save(*args, **kwargs)

        if self.image:
            user_img = Image.open(BytesIO(urlopen(self.image.url).read()))

            if user_img.width >= 351 or user_img.height >= 351:
                output_size = (350, 350)
                user_img.thumbnail(output_size)
                user_img.save(self.image.path)




# Signals for User/Profile
@receiver(post_save, sender=User)
def register_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()