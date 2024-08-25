from django.urls import path

from content.views import AjaxHandler

urlpatterns = [
    path('', AjaxHandler.as_view())
]