import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def handle_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"Created profile for new user: {instance}")
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()
            logger.info(f"Updated profile for user: {instance}")
        else:
            logger.warning(f"No profile found for user: {instance}")
