DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'super_db',
        'USER': 'usernews',
        'PASSWORD': '123qwe!news',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SECRET_KEY = 'Sn$hwU?EP&|/Q(G?L[o=:H.?$;jLiv{]gOScCD0?eC:KXa|ii*]o|~--YtO2yRz'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '64.227.68.31']