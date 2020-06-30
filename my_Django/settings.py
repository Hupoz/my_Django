"""
Django settings for my_Django project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.path.dirname获取该文件的父级目录，该指令为BASE_DIR等于setting.py文件的上上级目录，即根目录


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')6du4u#5=&ea+7%$ez&y9!e&n4(qa2b^j1g&4jlt!&mzq@-i4y'
# 加密函数-必需，密码重置，表单提交，csrf的key，session数据等都需要SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # 设置成False之后看不到详细错误提示

ALLOWED_HOSTS = []  # 为了限定请求中的host值，以防止黑客构造包来发送请求。只有在列表中的host才能访问
# 当DEBUG=False时，这个为必填项


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CardManage.apps.CardmangeConfig',
    'BookManage',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # 防止跨域请求的安全机制
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'my_Django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'  # 静态文件的路径别名，对外提供WEB访问时的URL地址


# STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')  # 部署时用到（python manage.py collectstatic）
# 执行collectstatic命令后会将项目中的静态文件（包括STATICFILES_DIRS、自带admin的静态文件）收集到该目录下面来（所以不应该在该目录下面放置自己的一些静态文件，因为会覆盖掉）
#
# # 当DEBUG设置成False之后,下面的STATICFILES_DIRS下的静态文件将会失效,需要STATIC_ROOT发挥作用：
#
# # 设置图片等静态文件的路径,开发阶段放置项目自己的静态文件（不能包含STATIC_ROOT路径）
# 该命令会告诉django,首先到STATICFILES_DIRS里面寻找静态文件，其次再到各个app的static文件夹里面找（惰性查找,查找到第一个,就停止查找了）
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),  # 这个静态文件的名称必须和项目里面的文件名称相同
    )                                  # STATICFILES_DIRS为元组或列表，“,”不可丢失！

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
