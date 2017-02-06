from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'champions', views.ChampionViewSet)
# router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
