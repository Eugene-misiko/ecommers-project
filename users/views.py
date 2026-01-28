from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, UserPrfile
from .serializers import CustomerSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

def create_profile(request):
    UserPrfile = UserPrfile.objects.create(
        username = 'Joseph',
        email = 'jay@example.com',
        ssn = '123-45-67-89',
        bio = 'This is a bio about Joseph.'
    )
    print(UserPrfile.ssn)
    print(UserPrfile.bio)   
    return render(UserPrfile, '')

