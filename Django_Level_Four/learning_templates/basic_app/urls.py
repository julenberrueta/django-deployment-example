from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app_html' # ESTE 'basic_app' es importante ya que tiene que coincidir con el que utilizamos en relative_url_templates.html

urlpatterns = [
    path(r"relative/", views.relative, name='relative_html'),
    path(r"other/", views.other, name='other_html')
]
