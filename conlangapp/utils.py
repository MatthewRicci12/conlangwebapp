from .models import *

def handle_form_submit(request, selected_form):
    if selected_form == "vocabulary_entry_form":
        part_of_speech = request.POST['part_of_speech']
        definition = request.POST['definition']
        vocabulary_entry = VocabularyEntry(part_of_speech=part_of_speech, definition=definition,
                                           tokens=request.POST['token'])
        vocabulary_entry.user = request.user if request.user.is_authenticated else None
        vocabulary_entry.save()

    elif selected_form == "glyph_form":
        glyph = Glyph(glyph_string=request.POST['token'])
        glyph.user = request.user if request.user.is_authenticated else None
        glyph.save()

    elif selected_form == "grammar_note_form":
        grammar_note_body = request.POST['body']
        grammar_note = GrammarNote(body=grammar_note_body, title=request.POST['token'])
        grammar_note.user = request.user if request.user.is_authenticated else None
        grammar_note.save()