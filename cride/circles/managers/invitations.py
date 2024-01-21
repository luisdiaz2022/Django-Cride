"""Circle invitations managers."""

# Django
from django.db import models

# Utilities
import random
from string import ascii_uppercase, digits

class InvitationManager(models.Manager):
    """Invitation Manager.
    
    Used to handle code creation.
    """

    def create(self, **kwargs):
        """Handle code creation.
        
        Used to handle code creation.
        """

        CODE_LENGTH = 10

        pool = ascii_uppercase + digits + '.-'
        code = kwargs.get('code', ''.join(random.choices(pool, k=self.CODE_LENGTH)))
        while self.filter(code=code).exists():
            code = ''.join(random.choices(pool, k=self.CODE_LENGTH))
        kwargs['code'] = code
        return super(InvitationManager, self).create(**kwargs)
        