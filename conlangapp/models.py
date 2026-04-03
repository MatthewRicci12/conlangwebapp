from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


#title = models.CharField(max_length=100, null=False, blank=False, default=None unique=False)
# null=False → Database column does NOT allow NULL
# default=None → Field is required (you must provide a value when creating an instance)
# blank=False → Form validation requires the field to be filled

class User(AbstractUser):
    email = models.EmailField(unique=True) #It checks format automatically
    # User handles password already
    user_id = models.AutoField(primary_key=True) #Not needed; Django adds automatically

class Token(models.Model):
    surface_form = models.CharField(max_length=255)
    token_id = models.AutoField(primary_key=True) #Not needed; Django adds automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=True, related_name="tokens")  # db_costraint True by default, says constraint SHOULD be created

class GrammarNote(models.Model):
    title = models.CharField(max_length=255, default=f"Grammar Note") #TODO Get index dynamically
    body = models.TextField()
    gn_id = models.AutoField(primary_key=True) #Not needed; Django adds automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=True, related_name="grammar_notes") #db_costraint True by default, says constraint SHOULD be created
    tokens = models.ManyToManyField(Token)


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

    definition = models.CharField(max_length=255)
    part_of_speech = models.IntegerField(choices=PartOfSpeech, default=PartOfSpeech.UNDECIDED)
    grammar_tag = models.CharField(max_length=255)
    ve_id = models.AutoField(primary_key=True)  # Not needed; Django adds automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=True, related_name="vocabulary_entries")  # db_costraint True by default, says constraint SHOULD be created
    tokens = models.ManyToManyField(Token)


class Text(models.Model):
    title = models.CharField(max_length=255, default="Title")  #TODO Get index dynamically
    body = models.TextField()
    date_added = models.DateTimeField(null=False, default=timezone.now)
    text_id = models.AutoField(primary_key=True)  # Not needed; Django adds automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=True, related_name="texts")  # db_costraint True by default, says constraint SHOULD be created



class PhonologyMapping(models.Model):
    class PhonologicalStatus(models.IntegerChoices):
        UNDECIDED = 0
        PHONEME = 1
        ALLOPHONE = 2
        FREE_VARIATION = 3

    ipa_symbol = models.CharField(null=True, max_length=10) #Probably have a palceholder or let it be null
    phonological_status = models.IntegerField(choices=PhonologicalStatus, default=PhonologicalStatus.UNDECIDED)
    distribution = models.CharField(null=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=True, related_name="phonology_mappings")  # db_costraint True by default, says constraint SHOULD be created
    pm_id = models.AutoField(primary_key=True)  # Not needed; Django adds automatically

class Glyph(models.Model):
    glyph_string = models.CharField(max_length=10)
    glyph_id = models.AutoField(primary_key=True)  # Not needed; Django adds automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=True, related_name="glyphs")  # db_costraint True by default, says constraint SHOULD be created
    phonology_mappings = models.ManyToManyField(PhonologyMapping)

# If any many-to-many pairings THEMSELVES have attributes, check out 4th normal form and make an explicit table, not default DJango.

#authors = models.ManyToManyField(Author)

# name = models.CharField(max_length=X)
# email = models.EmailField()
# created_at = models.DateTimeField(auto_now_add=True) (auto set timestamp, that option)

# user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts') so we can do #user.contacts.all()

# class Meta:
#     unique_together = ('user', 'email')

# Should do def__str__(self)


### python .\manage.py makemigrations
### python .\manage.py migrate
### Right click db.sqlite3

### I guess you should do superuser thing and add to admin