from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from io import BytesIO
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Profiles 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_img', storage=RawMediaCloudinaryStorage())
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Data'

    # Profile Image sizing and saving
    def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.image:
        img = Image.open(self.image)
        if img.width >= 351 or img.height >= 351:
            output_size = (350, 350)
            img.thumbnail(output_size)
            in_mem_file = BytesIO()
            img.save(in_mem_file, format='PNG')
            in_mem_file.seek(0)
            self.image = in_mem_file
            self.save(update_fields=['image'])



# Signals for User/Profile
@receiver(post_save, sender=User)
def register_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()