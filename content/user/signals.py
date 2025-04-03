from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Profile,User

@receiver(post_save, sender=Profile)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(
            username=instance.user.username,
            email=instance.user.email,
            phone_number=instance.user.phone_number
        )
@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.user.save()