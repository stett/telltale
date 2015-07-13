from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from stories.models import StoryChunk


@receiver(post_save, sender=StoryChunk)
def handle_loan_payment_missed(sender, instance, **kwargs):
    instance.story.update_current_author()
