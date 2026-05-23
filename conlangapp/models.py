from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True) #It checks format automatically
    # User handles password already
    user_id = models.AutoField(primary_key=True) #Not needed; Django adds automatically

class Token(models.Model):
    surface_form = models.CharField(max_length=255)

    token_id = models.AutoField(primary_key=True) #Not needed; Django adds automatically
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, db_constraint=True, related_name="tokens")  # db_costraint True by default, says constraint SHOULD be created

class GrammarNote(models.Model):
    title = models.CharField(max_length=255, default=f"Grammar Note") #TODO Get index dynamically
    body = models.TextField(blank=True)

    gn_id = models.AutoField(primary_key=True) #Not needed; Django adds automatically
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, db_constraint=True, related_name="grammar_notes") #db_costraint True by default, says constraint SHOULD be created
    tokens = models.CharField(max_length=255, default="")


class VocabularyEntry(models.Model):
    class PartOfSpeech(models.IntegerChoices):
        UNDECIDED = 0
        NOUN = 1
        VERB = 2
        ADJECTIVE = 3
        ADVERB = 4
        PRONOUN = 5
        ADPOSITION = 6
        CONJUNCTION = 7
        DETERMINER = 8
        INTERJECTION = 9
        PARTICLE = 10
        CLITIC = 11
        CLASSIFIER = 12
        DEMONSTRATIVE = 13

    tokens = models.CharField(max_length=255, default="")
    definition = models.CharField(max_length=255)
    part_of_speech = models.IntegerField(choices=PartOfSpeech, default=PartOfSpeech.UNDECIDED)

    grammar_tag = models.CharField(null=True, max_length=255) #No implementation yet
    ve_id = models.AutoField(primary_key=True)  # Not needed; Django adds automatically
    user = models.ForeignKey(User, default=None,  on_delete=models.CASCADE, db_constraint=True, related_name="vocabulary_entries")  # db_costraint True by default, says constraint SHOULD be created



class Text(models.Model):
    title = models.CharField(max_length=255, default="Title")  #TODO Get index dynamically
    body = models.TextField()

    date_added = models.DateTimeField(null=False, default=timezone.now)
    text_id = models.AutoField(primary_key=True)  # Not needed; Django adds automatically
    user = models.ForeignKey(User, default=None,  on_delete=models.CASCADE, db_constraint=True, related_name="texts")  # db_costraint True by default, says constraint SHOULD be created

class PhonologyMapping(models.Model):
    class PhonologicalStatus(models.IntegerChoices):
        UNDECIDED = 0
        PHONEME = 1
        ALLOPHONE = 2
        FREE_VARIATION = 3

    ipa_symbol = models.CharField(null=True, max_length=10)
    phonological_status = models.IntegerField(choices=PhonologicalStatus, default=PhonologicalStatus.UNDECIDED)
    distribution = models.CharField(null=True, max_length=255)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, db_constraint=True, related_name="phonology_mappings")
    pm_id = models.AutoField(primary_key=True)

class Glyph(models.Model):
    glyph_string = models.CharField(max_length=10)
    glyph_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=None,  on_delete=models.CASCADE, db_constraint=True, related_name="glyphs")
    phonology_mappings = models.ManyToManyField(PhonologyMapping, related_name="glyphs")