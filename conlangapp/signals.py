from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Glyph

@receiver(pre_delete, sender=Glyph)
def delete_related_phonology_mappings(sender, instance, **kwargs):
    for pm in instance.phonology_mappings.all():
        if pm.glyphs.count() == 1:
            pm.delete()