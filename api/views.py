from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import FooSerializer
from .models import Foo

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class FooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all().order_by('name')
    serializer_class = FooSerializer