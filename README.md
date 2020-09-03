# Django Rest Framework (DRF) - CRUD, Pagination, Search, Ordering
> Tutorial sederhana untuk memulai Rest API dengan Django

##### A. Referensi
- [Website Resmi](https://www.django-rest-framework.org/)

##### B. Kebutuhan
- [mysqlclient]
`` pip install mysqlclient``
- [djangorestframework] 
``pip install djangorestframework``
- [django-cors-headers] 
``pip install django-cors-headers``
- [django-filter] 
``pip install django-filter``

##### C. Langkah
1. Buat project baru DRF
``django-admin startproject drf``
2. Buat folder baru **apss** di root
3. Buat app baru di folder **drf/apps**
``django-admin startapp user``
4. Ubah config database di setting.py (sebelumnya buat database di MySQL)
- INSTALLED_APPS
    ```python
    ...
    ...
    'rest_framework',
    'corsheaders',
    'apps.user',
    ```
 - MIDDLEWARE
    ```python
    ...
    ...
    'corsheaders.middleware.CorsMiddleware',
    ```
- DATABASES
    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'learnenv',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',   
        'PORT': '3306',
        }
    }
    ```
 - REST_FRAMEWORK
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
    }
    ```
 - Tambahan
    ```python
    CORS_ORIGIN_ALLOW_ALL = True
    ```
5. Di folder ***root*** ketikkan perintah ini
- ``python manage.py makemigrations``
- ``python manage.py migrate``
- ``python manage.py runserver``
6. Di folder ***apps/user*** buat file baru : serializers.py
    ```python
    from rest_framework import serializers
    from django.contrib.auth.models import User
    class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = (
			'url',
			'id',
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			'date_joined',
			)

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user
		
	def update(self, instance, validated_data):
		fields=instance._meta.fields
		exclude=[]
		for field in fields:
			field=field.name.split('.')[-1]
			if field in exclude:
				continue
			exec("instance.%s = validated_data.get(field, instance.%s)"%(field,field))
		if validated_data.get('password') :
			instance.set_password(validated_data.get('password', instance.password) )
		instance.save()
		return instance
    ```
7. Di folder ***apps/user*** buat file baru : urls.py
    ```python
    from django.urls import include, path
    from rest_framework import routers
    from .views import *
    
    router = routers.DefaultRouter()
    router.register(r'users', UserViewSet)
    
    urlpatterns = [
    	path('', include(router.urls)),
    ]
    ```
