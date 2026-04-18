from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_text", views.submit_text, name="submit-text"),
    path("handle_file", views.handle_file, name="handle-file"),
    path("enter_text", views.enter_text_screen, name="enter-text"),

    path('user_clicks_text/<int:text_id>/', views.user_clicks_text, name="user-clicks-text"),
    path('user_clicks_text/<int:text_id>/submit_token', views.submit_token, name="submit-token"),

    path('crud_router', views.crud_router, name="crud-router"),
    path('modal', views.modal, name="modal"),
    path('create_phonology_mapping', views.create_phonology_mapping, name="create-phonology-mapping"),

    path("vocabulary_list", views.vocabulary_list, name="vocabulary-list"),
    path("phonology_and_glyphs_tab", views.phonology_and_glyphs_tab, name="phonology-and-glyphs-tab"),
    path("grammar_tab", views.grammar_tab, name="grammar-tab"),
]