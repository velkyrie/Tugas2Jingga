# TODO: Implement Routings Here
from django.urls import path
from example_app.views import index
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]