from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from .forms import *
from pathlib import Path

#@login_required

def index(request):
    context = {}
    texts = Text.objects.all().order_by('-date_added')
    submit_text_form = SubmitTextForm()
    upload_file_form = UploadFileForm()
    context = {
        'texts': texts,
        'submit_text_form': submit_text_form,
        'upload_file_form': upload_file_form
    }
    return render(request, 'index.html', context)

@require_http_methods(['POST'])
def submit_text(request):
    form = SubmitTextForm(request.POST)
    x = 3
    if form.is_valid():
        text = form.save(commit=False)
        if text.user:
            text.user = request.user
        else:
            text.user = None
        #TODO: Save datetime too
        text.save()
        context = {'text': text}
        response = render(request, 'partials/text-entry.html', context)
        return response
    else:
        return HttpResponse(status=405)

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
            date_added=timezone.now(),  # Resolves your datetime TODO
        )
        text.save()

        context = {'text': text}
        response = render(request, 'partials/text-entry.html', context)
        return response
    else:
        return HttpResponse(status=405)

def submit_token(request, text_id):
    pass #TODO


def enter_text_screen(request):
    return render(request, 'enter_text_screen.html')

def user_clicks_text(request, text_id):
    text_content = Text.objects.get(text_id=text_id).body
    context = {'text_content': text_content, 'text_id': text_id}
    return render(request, 'extract_text.html', context)

def vocabulary_list(request):
    return render(request, 'vocabulary_list.html')

def phonology_and_glyphs_tab(request):
    return render(request, 'phonology_and_glyphs_tab.html')

def grammar_tab(request):
    return render(request, 'grammar_tab.html')