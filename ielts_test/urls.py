from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ielts_test import views

router = DefaultRouter()

router.register(r'ielts-tests', views.IeltsTestViewSet)
router.register(r'ielts-questions', views.IeltsQuestionsViewSet)
router.register(r'ielts-answers', views.IeltsAnswersTestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
