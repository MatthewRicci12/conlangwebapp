from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import *
from pathlib import Path
from .crud.crud import *
import json

crud_map = {
    ('Text', 'update'): update_text,
    ('Text', 'delete'): delete_text,
    ('GrammarNote', 'update'): update_grammarnote,
    ('GrammarNote', 'delete'): delete_grammarnote,
    ('VocabularyEntry', 'update'): update_vocabularyentry,
    ('VocabularyEntry', 'delete'): delete_vocabularyentry,
    ('Glyph', 'update'): update_glyph,
    ('Glyph', 'delete'): delete_glyph,
}

def index(request):
    if request.method == 'POST':
        submit_text_form = SubmitTextForm(request.POST)
        if submit_text_form.is_valid():
            text = submit_text_form.save(commit=False)
            text.user = request.user if text.user else None
            text.save()
            return redirect('index')
    else:
        submit_text_form = SubmitTextForm()

    if 'primary_key' in request.POST:
        model = "Text"
        action = "update"
        primary_key = int(request.POST['primary_key'])
        params = {}
        if 'params' in request.POST:
            params = json.loads(request.POST['params'])
        crud_router(model, action, primary_key, params)

    if 'primary_key' in request.GET:
        model = "Text"
        action = "delete"
        primary_key = int(request.GET['primary_key'])
        params = {'primary_key': primary_key}
        crud_router(model, action, primary_key, params)

    texts = Text.objects.all().order_by('-date_added')
    upload_file_form = UploadFileForm()
    context = {
        'texts': texts,
        'submit_text_form': submit_text_form,
        'upload_file_form': upload_file_form,
    }
    return render(request, 'index.html', context)


# TODO: Better way to do this handoff? Perhaps with a common helper function?
@require_http_methods(['POST'])
def handle_file(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_file = form.cleaned_data['file']

        file_name_stripped = Path(uploaded_file.name).stem
        file_contents = uploaded_file.read().decode('utf-8')

        text = Text(
            title=file_name_stripped,
            body=file_contents,
            date_added=timezone.now(),
        )
        text.save()

        context = {'text': text}
        response = render(request, 'partials/text_entry.html', context)
        return response
    else:
        return HttpResponse(status=405)

def submit_token(request, text_id):
    return render(request, 'partials/current_form.html')


def enter_text_screen(request):
    return render(request, 'enter_text_screen.html')

def user_clicks_text(request, text_id):
    text_content = Text.objects.get(text_id=text_id).body
    form_div_context = {'text_id': text_id}
    vocabulary_entry_form = VocabularyEntryForm(request.POST)
    glyph_form = GlyphForm(request.POST)
    grammar_note_form = GrammarNoteForm(request.POST)

    if 'form_up' in request.POST:
        form_up = True
        form_div_context['vocabulary_entry_form'] = vocabulary_entry_form
        form_div_context['glyph_form'] = glyph_form
        form_div_context['grammar_note_form'] = grammar_note_form
    else:
        form_up = False

    if 'token' in request.POST:
        token = request.POST['token']
        form_div_context['token'] = token
    else:
        form_div_context['token'] = ''

    if 'selected_form' in request.POST:
        selected_form = request.POST['selected_form']
        form_div_context['selected_form'] = selected_form

        if "form_has_been_submitted" in request.POST:

            if selected_form == "vocabulary_entry_form":
                part_of_speech = request.POST['part_of_speech']
                definition = request.POST['definition']
                vocabulary_entry = VocabularyEntry(part_of_speech=part_of_speech, definition=definition, tokens=request.POST['token'])
                vocabulary_entry.save()

            elif selected_form == "glyph_form":
                glyph = Glyph(glyph_string=request.POST['token'])
                glyph.save()

            elif selected_form == "grammar_note_form":
                grammar_note_body = request.POST['body']
                grammar_note = GrammarNote(body=grammar_note_body, title=request.POST['token'])
                grammar_note.save()

    else:
        form_div_context['selected_form'] = ''

    context = {'text_content': text_content, 'text_id': text_id, 'form_up': form_up, 'params': {'text_id': text_id, 'form_up': form_up, 'selected_form': form_div_context['selected_form']},
               'form_div_context': form_div_context}
    return render(request, 'extract_text.html', context)


def vocabulary_list(request):
    context = {'ves': []}
    for ve in VocabularyEntry.objects.all():
        context['ves'].append(ve)

    if 'primary_key' in request.POST:
        model = "Text"
        action = "update"
        primary_key = int(request.POST['primary_key'])
        params = {}
        if 'params' in request.POST:
            params = json.loads(request.POST['params'])
        crud_router(model, action, primary_key, params)

    if 'primary_key' in request.GET:
        model = "Text"
        action = "delete"
        primary_key = int(request.GET['primary_key'])
        params = {'primary_key': primary_key}
        crud_router(model, action, primary_key, params)

    return render(request, 'vocabulary_list.html', context)


def create_phonology_mapping(request):
    selected_ipa_symbol = request.POST['selected_ipa_symbol']
    selected_glyph_pk = request.POST['selected_glyph_pk']
    pm = PhonologyMapping(ipa_symbol=selected_ipa_symbol)
    pm.save()
    glyph = Glyph.objects.get(pk=selected_glyph_pk)
    glyph.phonology_mappings.add(pm)


def phonology_and_glyphs_tab(request):
    context = {'glyphs': []}
    for glyph in Glyph.objects.all():
        context['glyphs'].append(glyph)

    currently_selected_glyph_id = None
    if 'glyph_id' in request.POST:
        if request.POST['glyph_id'] != 'null':
            currently_selected_glyph_id = int(request.POST['glyph_id'])
    context['currently_selected_glyph_id'] = currently_selected_glyph_id

    selected_ipa_symbol = None
    if 'selected_ipa_symbol' in request.POST:
        create_phonology_mapping(request)
        selected_ipa_symbol = request.POST['selected_ipa_symbol']
        context['currently_selected_glyph_id'] = None
    context['selected_ipa_symbol'] = selected_ipa_symbol

    if 'primary_key' in request.POST:
        model = "Text"
        action = "update"
        primary_key = int(request.POST['primary_key'])
        params = {}
        if 'params' in request.POST:
            params = json.loads(request.POST['params'])
        crud_router(model, action, primary_key, params)

    if 'primary_key' in request.GET:
        model = "Text"
        action = "delete"
        primary_key = int(request.GET['primary_key'])
        params = {'primary_key': primary_key}
        crud_router(model, action, primary_key, params)

    return render(request, 'phonology_and_glyphs_tab.html', context)

def grammar_tab(request):
    context = {'gns': []}
    for gn in GrammarNote.objects.all():
        context['gns'].append(gn)

    if 'primary_key' in request.POST:
        model = "Text"
        action = "update"
        primary_key = int(request.POST['primary_key'])
        params = {}
        if 'params' in request.POST:
            params = json.loads(request.POST['params'])
        crud_router(model, action, primary_key, params)

    if 'primary_key' in request.GET:
        model = "Text"
        action = "delete"
        primary_key = int(request.GET['primary_key'])
        params = {'primary_key': primary_key}
        crud_router(model, action, primary_key, params)

    return render(request, 'grammar_tab.html', context)

def crud_router(model, action, primary_key, params):
    params['primary_key'] = primary_key
    crud_map[(model, action)](params)

@require_http_methods(["GET"])
def modal(request):
    pk = request.GET['primary_key']
    model = request.GET['model']

    context = {}

    if model == "Glyph":
        context = {'which_model': 'Glyph', 'pk': pk, 'form': GlyphForm(request.POST)}

    if model == "Text":
        context = {'which_model': 'Text', 'pk': pk, 'form': SubmitTextForm(request.POST)}

    if model == "VocabularyEntry":
        context = {'which_model': 'VocabularyEntry', 'pk': pk, 'form': VocabularyEntryForm(request.POST)}

    if model == "GrammarNote":
        context = {'which_model': 'GrammarNote', 'pk': pk, 'form': GrammarNoteForm(request.POST)}

    return render(request, 'partials/modal.html', context=context)