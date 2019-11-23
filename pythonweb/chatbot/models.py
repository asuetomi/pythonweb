from django.db import models

# Create your models here.

class Response(models.Model):
    """応答"""
    keyword = models.CharField(max_length = 255, primary_key = True)
    text = models.CharField(max_length = 255)

    # class Meta:
    #     verbose_name = _("response")
    #     verbose_name_plural = _("responses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("response_detail", kwargs={"pk": self.pk})

class words(models.Model):
    """単語の意味"""
    word = models.CharField(max_length = 255, primary_key = True)
    mean = models.CharField(max_length = 255)

    # class Meta:
    #     verbose_name = _("words")
    #     verbose_name_plural = _("wordss")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("words_detail", kwargs={"pk": self.pk})


class siritori(models.Model):
    """しりとり用の単語辞書"""
    ruby = models.CharField(max_length = 255)
    word = models.CharField(max_length = 255)
    used = models.IntegerField()

    # class Meta:
    #     verbose_name = _("siritori")
    #     verbose_name_plural = _("siritoris")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("siritori_detail", kwargs={"pk": self.pk})
