# urls.py
from rest_framework.routers import SimpleRouter, DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet

# Создаётся роутер
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами url и вьюхой
# слеш не ставим после имени ! no cats/ just cats
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]

