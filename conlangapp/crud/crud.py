from ..models import *

# DONE
def update_text(params):
    text_id = params.get('primary_key')
    title = params.get('title')
    body = params.get('body')
    text_to_update = Text.objects.get(pk=text_id)
    text_to_update.title = title
    text_to_update.body = body
    text_to_update.save()

# DONE
def delete_text(params):
    text_id = params.get('primary_key')
    text_to_delete = Text.objects.get(pk=text_id)
    text_to_delete.delete()

# DONE
def update_grammarnote(params):
    gn_id = params.get('primary_key')
    body = params.get('body')
    grammarnote_to_update = GrammarNote.objects.get(pk=gn_id)
    grammarnote_to_update.body = body
    grammarnote_to_update.save()

# DONE
def delete_grammarnote(params):
    gn_id = params.get('primary_key')
    grammarnote_to_delete = GrammarNote.objects.get(pk=gn_id)
    grammarnote_to_delete.delete()

# DONE
def update_vocabularyentry(params):
    ve_id = params.get('primary_key')
    definition = params.get('definition')
    part_of_speech = params.get('part_of_speech')
    ve_to_update = VocabularyEntry.objects.get(pk=ve_id)
    ve_to_update.definition = definition
    ve_to_update.part_of_speech = part_of_speech
    ve_to_update.save()

# DONE
def delete_vocabularyentry(params):
    ve_id = params.get('primary_key')
    ve_to_delete = VocabularyEntry.objects.get(pk=ve_id)
    ve_to_delete.delete()

# DONE
def update_glyph(params):
    glyph_id = params.get('primary_key')
    new_glyph_string = params.get('glyph_string')
    glyph_to_update = Glyph.objects.get(pk=glyph_id)
    glyph_to_update.glyph_string = new_glyph_string
    glyph_to_update.save()

# DONE
def delete_glyph(params):
    glyph_id = params.get('primary_key')
    glyph_to_delete = Glyph.objects.get(pk=glyph_id)

    for pm in glyph_to_delete.phonology_mappings.all():
        if pm.glyphs.count() == 1:
            pm.delete()

    glyph_to_delete.delete()