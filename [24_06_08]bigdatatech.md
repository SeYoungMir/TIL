# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 3. 장고 어드민 사용하기
3. 스크립트 수정. - 코드
   - ```python
        """Django settings for book_db project
        Generated by 'django-admon startproject' using Django 2.1.7

        For more information on this file, see https://docs.djangoproject.com/en/2.1/topics/settings/

        For the full list of settings and their values, see https://docs.djagoproject.com/en/2.1/ref/settings/
        """
        import os

         # Build paths inside the project lisk this : os.path.join(BASE_DIR,...)
        BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file)))

         # Quick-start development settings - unsuitable for production
        # See https://docs.djangoproject.com/en.2.1/howto/depolyment/checklist

        # SECURITY WARNING: keep the secret key used in production secret!
        SECRET_KEY = '(중략)'

        # SECURITY WARNING: don't run with debug turned on in production!
        DEBUG = True

        ALLOWED_HOSTS = ['*']

        # Application definition

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            'book.apps.BookConfig',
    
        ]
        MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

        ROOT_URLCONF = 'book_db.urls'

        
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [],
                # 'DIRS': [],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

        WSGI_APPLICATION = 'book_db.wsgi.application'
        # Database
        # https://docs.djangoproject.com/en/4.1/ref/settings/#databases
        
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'localhost',
            'NAME': 'book_db',
            'USER': 'root',
            'PASSWORD': '',
            }
        }

            # Password validation
        # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

        AUTH_PASSWORD_VALIDATORS = [
            {
                'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
            },
        ]

        # Internationalization
        # https://docs.djangoproject.com/en/4.1/topics/i18n/

        LANGUAGE_CODE = 'en-us'
        TIME_ZONE = 'UTC'

        USE_I18N = True

        USE_L10N = True

        USE_TZ = True

        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/4.1/howto/static-files/

        STATIC_URL = 'static/'
      ```
   - 프로젝트 이름(book_db/book_db) 바로 아래의 settings.py에는 장고의 종합적인 설정 작성.