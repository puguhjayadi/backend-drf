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
``python manage.py makemigrations``
``python manage.py migrate``
``python manage.py runserver``




