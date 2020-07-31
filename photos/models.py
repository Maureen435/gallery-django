from django.db import models

class Images(models.Model):
    name = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    image_location = models.ForeignKey('location', on_delete=models.CASCADE,)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE,)

    @classmethod
    def search_image(cls,category):
        images = cls.objects.filter(image_category_name = category )
        return images