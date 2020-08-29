from rest_framework import viewsets, filters, pagination
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	pagination.PageNumberPagination.page_size_query_param = 'page_size' 

	filter_backends = [
	filters.SearchFilter,
	filters.OrderingFilter,
	]

	search_fields = ['username','first_name','last_name','email']
	ordering_fields = '__all__'