from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse
import re

register = template.Library()

@register.filter
def hoverable_words(text, text_id):
    words = re.split(r'(\s+)', text)  # preserves whitespace
    result = ''
    for token in words:
        if token.strip():
            url = reverse('submit-token', args=[text_id])
            result += f'<span class="word" hx-post="{url}" hx-vals=\'{{"token": "{token}"}}\'>{token}</span>'
        else:
            result += token
    return mark_safe(result)