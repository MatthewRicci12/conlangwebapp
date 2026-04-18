from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse
import re

register = template.Library()

@register.filter
def hoverable_words(text, params):
    text_id = params.get('text_id')
    selected_form = params.get('selected_form')
    words = re.split(r'(\s+)', text)  # preserves whitespace
    result = ''
    for token in words:
        if token.strip():
            url = reverse('user-clicks-text', args=[text_id])
            #result += f'<span class="word" hx-post="{url}" hx-target="body" hx-vals=\'{{ "form_up": 1, "token": "{token}", "selected_form": "{selected_form}" }}\'>{token}</span>'
            result += f'<span class="word"}}\'>{token}</span>'
        else:
            result += token
    return mark_safe(result)