from django import template

part_of_speech_enum = {
    0: "Undecided",
    1: "Noun",
    2: "Verb",
    3: "Adjective",
    4: "Adverb",
    5: "Pronoun",
    6: "Adposition",
    7: "Conjunction",
    8: "Determiner",
    9: "Interjection",
    10: "Particle",
    11: "Clitic",
    12: "Classifier",
    13: "Demonstrative",
}

register = template.Library()

@register.filter
def get_part_of_speech(pos_value):
    return part_of_speech_enum[pos_value]