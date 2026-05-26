from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import GemListing
from .serializers import GemListingSerializer

class GemListingViewSet(viewsets.ModelViewSet):
    queryset = GemListing.objects.all()
    serializer_class = GemListingSerializer
    permission_classes = [AllowAny]

    def get_by_owner(self, request, owner_id=None):
        """
        Returns all gem listings associated with a specific owner_id passed as a path param.
        """
        if not owner_id:
            return Response(
                {"error": "owner_id path parameter is required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        owner_gems = self.queryset.filter(owner_id=owner_id)
        serializer = self.get_serializer(owner_gems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)