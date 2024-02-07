# views.py
from rest_framework import viewsets
from .models import invoiceHeader
from .serializers import invoiceHeaderSerializer

class InvoiceHeaderViewset(viewsets.ModelViewSet):
    queryset = InvoiceHeader.objects.all()
    serializer_class = invoiceHeaderSerializer

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
