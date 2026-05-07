from rest_framework import viewsets
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    permission_classes = [AllowAny]



class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    permission_classes = [AllowAny]

