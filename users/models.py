from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
import cloudinary
from io import BytesIO
import requests

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

    # Open the image from Cloudinary using the image URL
    response = requests.get(self.image.url)
    user_img = Image.open(BytesIO(response.content))
    
    # If the image uploaded is more or equals to 351px, set it to 350px and save it
    if user_img.width >= 351 or user_img.height >= 351:
        output_size = (350, 350)
        user_img.thumbnail(output_size)

        # Create a BytesIO object to store the modified image
        image_io = BytesIO()
        user_img.save(image_io, format='JPEG')

        # Generate a unique filename
        filename = f"profile_img/{self.user.username}_avatar.jpg"

        # Upload the modified image to Cloudinary
        cloudinary_image = cloudinary.uploader.upload(image_io.getvalue(), public_id=filename)

        # Update the image field with the Cloudinary image URL
        self.image = cloudinary_image['secure_url']

        # Save the model instance with the updated image URL
        super().save(*args, **kwargs)


# Signals for User/Profile
@receiver(post_save, sender=User)
def register_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()