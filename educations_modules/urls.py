from django.contrib import admin
from django.urls import path, include

from modules.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'sections', SectionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # доступны методы GET и POST
    path('api/education_modules_list/', Edu_ModuleList.as_view()),
    # доступны методы GET, PUT, DELETE
    path('api/education_modules_detail/<int:pk>/', Edu_ModuleDetail.as_view()),
    # доступны метобы GET и POST
    # path('api/section/', SectionViewSet.as_view({'get': 'list', 'post': 'create'})),
    # доступны метобы GET, PUT и DELETE
    # path('api/section/<int:pk>/', SectionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/', include(router.urls))
]
