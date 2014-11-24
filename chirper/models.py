from django.db import models
from django.conf import settings

from django_stormpath.models import StormpathUser
from django_stormpath.models import CLIENT


class Chirp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField(max_length=160, verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True)
    owner_is_admin = models.BooleanField(default=False)
    owner_is_premium = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']


class ChirperUser(StormpathUser):

    def is_premium(self):
        premium_group = CLIENT.groups.get(settings.STORMPATH_PREMIUM_GROUP)
        return len(premium_group.accounts.search({'email': self.email}))

