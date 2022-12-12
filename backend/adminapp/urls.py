from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)

urlpatterns=[
    path('some', views.getsomething, name="something"),
    path("admin_auth/register", views.AdminUserView.as_view({
        "post": "create"}))
]
urlpatterns += router.urls