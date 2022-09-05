from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # This method runs after the model is saved
    # It reduces the size of an uploaded image
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.wodth > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
