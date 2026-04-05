from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_text", views.submit_text, name="submit-text"),
    path("handle_file", views.handle_file, name="handle-file"),
    path("enter_text", views.enter_text_screen, name="enter-text"),

    path('user_clicks_text/<int:text_id>/', views.user_clicks_text, name="user-clicks-text"),

    path("vocabulary_list", views.vocabulary_list, name="whatisthisnamefor3"),
    path("phonology_and_glyphs_tab", views.phonology_and_glyphs_tab, name="whatisthisnamefor4"),
    path("grammar_tab", views.grammar_tab, name="whatisthisnamefor5"),
]