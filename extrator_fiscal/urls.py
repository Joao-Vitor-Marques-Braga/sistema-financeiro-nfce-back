# apps/extrator_fiscal/urls.py

from django.urls import path
from .views import ExtratorFiscalAPIView

urlpatterns = [
    # A URL será /api/extrator/upload/
    path('upload/', ExtratorFiscalAPIView.as_view(), name='extrator-fiscal-upload'),
]