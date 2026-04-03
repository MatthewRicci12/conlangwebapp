from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
#
# def enter_text_screen(request):
#     return render(request, 'enter_text_screen.html')
#
# def user_clicks_text(request):
#     return render(request, 'user_clicks_text.html')
#
# def vocabulary_list(request):
#     return render(request, 'vocabulary_list.html')
#
# def phonology_and_glyphs_tab(request):
#     return render(request, 'phonology_and_glyphs_tab.html')
#
# def grammar_tab(request):
#     return render(request, 'grammar_tab.html')