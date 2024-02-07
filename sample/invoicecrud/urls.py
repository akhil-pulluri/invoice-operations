from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceHeaderViewset

router = DefaultRouter()
router.register(r'invoices', InvoiceHeaderViewset)

urlpatterns = [
    path('', include(router.urls)),
]
