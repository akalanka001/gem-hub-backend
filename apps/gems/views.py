from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import GemListing
from .serializers import GemListingSerializer
from apps.core.permissions import IsOwner, IsAdminUser

class GemListingViewSet(viewsets.ModelViewSet):
    queryset = GemListing.objects.all()
    serializer_class = GemListingSerializer

    def get_permissions(self):
        """
        Dynamically limits access. Anyone can browse all gems or view a specific gem.
        Everything else (creating, editing, deleting, or fetching by owner) requires a token.
        """
        
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsOwner(field_name='owner'), IsAdminUser]
            
        return [permission() for permission in permission_classes]

    def get_by_owner(self, request, owner_id=None):
        """
        Returns all gem listings associated with a specific owner_id.
        (Requires Supabase Authentication because of get_permissions)
        """
        if not owner_id:
            return Response(
                {"error": "owner_id path parameter is required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        owner_gems = self.queryset.filter(owner_id=owner_id)
        serializer = self.get_serializer(owner_gems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)