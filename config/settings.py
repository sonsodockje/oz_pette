import os
import environ
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")
NAVER_REST_API_KEY = env("NAVER_REST_API_KEY")
NAVER_ADMIN_KEY = env("NAVER_ADMIN_KEY")
NAVER_REST_API_SECRET = env("NAVER_REST_API_SECRET")  # 이 부분 추가

# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

THIRD_PARTY_APPS = [
    "rest_framework",
    # "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "colorfield",
    "whitenoise",
]

CUSTOM_APPS = [
    "users.apps.UsersConfig",
    "common.apps.CommonConfig",
]

SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),  # PostgreSQL 컨테이너에서 설정한 환경 변수를 가져옵니다.
        'USER': env('POSTGRES_USER'),  # PostgreSQL 컨테이너에서 설정한 환경 변수를 가져옵니다.
        'PASSWORD': env('POSTGRES_PASSWORD'),  # PostgreSQL 컨테이너에서 설정한 환경 변수를 가져옵니다.
        'HOST': 'localhost',  # Docker Compose 내부에서는 'localhost'가 아니라 'db'로 연결해야 합니다.
        'PORT': '5432',  # PostgreSQL의 기본 포트는 5432입니다.
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

DATE_INPUT_FORMATS = ["%Y-%m-%d"]

DATE_FORMAT = "F j"

USE_I18N = False

USE_TZ = False

AUTH_USER_MODEL = "users.User"

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "jwt",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True  # 모든 호스트 허용

CORS_ALLOW_ALL_ORIGINS = True

# 리액트와 연결 시 필요한 설정
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5713",
    "http://localhost:5713",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5713",
    "http://localhost:5713",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

# JWT settings
REST_USE_JWT = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),  # 토큰 유효 시간
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # 리프레시 토큰 유효 시간
    "ROTATE_REFRESH_TOKENS": False,  # 새로고침 토큰 사용 여부
    "BLACKLIST_AFTER_ROTATION": True,  # 블랙리스트 사용 여부
    "SIGNING_KEY": SECRET_KEY,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": None,
    "UPDATE_LAST_LOGIN": True,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_CLAIM": "email",  # 사용자의 아이디 JWT 토큰에 저장할 필드
    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.UntypedToken",
        "rest_framework_simplejwt.tokens.AccessToken",
    ),
    "TOKEN_TYPE_CLAIM": "token_type",  # 토큰 타입 필드
    "JTI_CLAIM": "jti",  # JWT ID 필드
    "TOKEN_USER_CLASS": "users.User",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=30),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/app/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

## 이메일 인증 시작 ##
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # 메일을 보내는 방식
EMAIL_HOST = env("EMAIL_HOST")  # 메일을 호스트 하는 서버
EMAIL_PORT = 587  # 메일과 통신하는 포트
EMAIL_USE_TLS = True  # TLS 보안 사용
EMAIL_HOST_USER = env("EMAIL_HOST_USER")  # 발신할 네이버 이메일
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # 네이버 앱 비밀번호
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 사이트와 관련한 자동 응답 받을 이메일 주소

ACCOUNT_AUTHENTICATION_METHOD = "email"  # 로그인시 username 이 아니라 email을 사용하게 하는 설정
ACCOUNT_EMAIL_REQUIRED = True  # 회원가입시 필수 이메일을 필수항목으로 만들기
ACCOUNT_USERNAME_REQUIRED = False  # USERNAME 을 필수항목에서 제거
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # 이메일 인증을 필수로 설정
ACCOUNT_EMAIL_ON_GET = True  # 이메일 인증시 이메일을 보내줌
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[회원가입 이메일 인증] "  # 이메일에 자동으로 표시되는 제목
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # 유저가 받은 링크를 클릭하면 회원가입 완료

URL_FRONT = (
    "http://127.0.0.1:5713",
)  # 프론트 주소

## 이메일 인증 끝 ##

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True  # 비밀번호 지워지지않음
ACCOUNT_SESSION_REMEMBER = True  # 브라우저를 닫아도 세션기록 유지! [ 로그인 안풀리게 ! ]
SESSION_COOKIE_AGE = 3600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
