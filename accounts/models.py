from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(
        'auth.user',
        unique=True,
        on_delete=models.CASCADE,
    )
    nickname = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    GENDER_SELECT = (
      ('男性', '男性'),
      ('女性', '女性'),
      ('非公開', '非公開'),
    )
    gender = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        choices=GENDER_SELECT,
        default='非公開'
    )
    introduction = models.TextField(
        max_length=140,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'pk':self.user_id})


