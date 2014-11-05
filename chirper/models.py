from django.db import models
from django.conf import settings
from django_stormpath.models import StormpathUser
from stormpath.client import Client

CLIENT = Client(id=settings.STORMPATH_ID,
            secret=settings.STORMPATH_SECRET)


class Chirp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField(max_length=160, verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True)
    owner_is_admin = models.BooleanField(default=False)
    owner_is_premium = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']


class ChirperUser(StormpathUser):

    def is_admin(self):
        admin_group = CLIENT.groups.get(settings.STORMPATH_ADMINISTRATORS)
        return len(admin_group.accounts.search({'email': self.email}))

    def is_premium(self):
        premium_group = CLIENT.groups.get(settings.STORMPATH_PREMIUMS)
        return len(premium_group.accounts.search({'email': self.email}))
