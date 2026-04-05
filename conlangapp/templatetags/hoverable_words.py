from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def hoverable_words(text):
    words = re.split(r'(\s+)', text)  # preserves whitespace
    result = ''
    for token in words:
        if token.strip():
            result += f'<span class="word">{token}</span>'
        else:
            result += token
    return mark_safe(result)