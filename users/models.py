from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
import cloudinary

# Profiles 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_img/default.jpg', upload_to='profile_img')
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Data'

    # Profile Image sizing and saving
    def save(self, *args, **kwargs):
        super().save()

        # Open the image using the Cloudinary SDK
        cloudinary.config(
            cloud_name='dmbdqco85',
            api_key='572555385744258',
            api_secret='0COw3jIp0nWL_2Lzjn7KTeGgihM'
        )
        cloudinary_image = cloudinary.uploader.upload(self.image.path)

        # Update the image field with the Cloudinary image URL
        self.image = cloudinary_image['secure_url']

        # If the image uploaded is more or equals to 351px, set it to 350px and save it
        user_img = Image.open(self.image.path)
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