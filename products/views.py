from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response

class ProductPagination(PageNumberPagination):
    page_size = 5  # Number of items per page
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination  # Add pagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Enable filtering and ordering
    search_fields = ['name', 'description']  # Fields to search through
    ordering_fields = ['price', 'created_at']  # Fields you can order by
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    def get():
        pass

class ExampleView(APIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    def get(self, request):
        return Response({'message' : 'This is a rate limited view4'})  

      
    


