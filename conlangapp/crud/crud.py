from ..models import *

def update_text(params):
    text_id = params.get('text_id')
    text_to_update = Text.objects.get(pk=text_id)
    print("update_text")

def delete_text(params):
    text_id = params.get('text_id')
    text_to_delete = Text.objects.get(pk=text_id)
    text_to_delete.delete()
    print("delete_text")

def update_grammarnote(params):
    gn_id = params.get('gn_id')
    grammarnote_to_update = GrammarNote.objects.get(pk=gn_id)
    print("update_grammarnote")

def delete_grammarnote(params):
    gn_id = params.get('gn_id')
    grammarnote_to_delete = GrammarNote.objects.get(pk=gn_id)
    grammarnote_to_delete.delete()
    print("delete_grammarnote")

def update_vocabularyentry(params):
    ve_id = params.get('ve_id')
    ve_to_update = VocabularyEntry.objects.get(pk=ve_id)
    print("update_vocabularyentry")

def delete_vocabularyentry(params):
    ve_id = params.get('ve_id')
    ve_to_delete = VocabularyEntry.objects.get(pk=ve_id)
    ve_to_delete.delete()
    print("delete_vocabularyentry")

def update_glyph(params):
    glyph_id = params.get('glyph_id')
    new_glyph_string = params.get('new_glyph_string')
    glyph_to_update = Glyph.objects.get(pk=glyph_id)
    glyph_to_update.glyph_string = new_glyph_string
    glyph_to_update.save()
    print("update_glyph")

def delete_glyph(params):
    glyph_id = params.get('glyph_id')
    glyph_to_delete = Glyph.objects.get(pk=glyph_id)
    glyph_to_delete.delete()
    print("delete_glyph")