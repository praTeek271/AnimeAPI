from django.db import models



class AnimeName(models.Model):
    name=models.CharField(max_length=300, primary_key=True)

    def __str__(self):
        return self.name


class url_location(models.Model):
    name=models.ForeignKey(AnimeName, on_delete=models.CASCADE)
    url1= models.CharField(max_length=500)
    url2= models.CharField(max_length=500)
    url3= models.CharField(max_length=500)

    def __str__(self):
        return self.name

class url_trailer(models.Model):
    name=models.ForeignKey(AnimeName, on_delete=models.CASCADE)
    url1= models.CharField(max_length=500)
    url2= models.CharField(max_length=500)

    def __str__(self):
        return self.name




class Anime(models.Model):
    name=models.ForeignKey(AnimeName, on_delete=models.CASCADE)
    anime_image = models.ImageField(upload_to='anime/images/')
    watch_url = models.ForeignKey(url_location, on_delete=models.CASCADE)
    hashtags = models.CharField(max_length=300)
    description = models.TextField()
    trailer_url = models.ForeignKey(url_trailer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


