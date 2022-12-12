from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer, AdminUserSerializer
from .models import AdminUser, User
import datetime


# Create your views here.


@api_view(['GET'])
def getsomething(request):
    return Response('Hell0')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class AdminUserView(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

    def create(self, request, *args, **kwargs):
        now_date = datetime.datetime.now().strftime("%d-%m-%Y")
        now_time = datetime.datetime.now().strftime("%H:%M:%S")
        if request.user.is_staff:
            data = request.data
            data['role'] = "admin"
            data["password"] = "Pak1235"
            check_user = User.objects.filter(email=data['email']).first()
            if check_user:
                user = UserSerializer(data=data)
                if user.is_valid(raise_exception=True):
                    user.save()
                    user.set_password(data['password'])
                    user.save()
                    data[user] = user.id
                    user_profie = AdminUserSerializer(data=data)
                    if user_profie.is_valid(raise_exception=True):
                        user_profie.save()
                        return Response({"msg": "Admin has been created Successfully"}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({
                            'message': user_profie.errors
                        }, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({
                        'message': user.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "message": "User has been already there"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "message": "only Super Admin can create this user!"
            }, status=status.HTTP_400_BAD_REQUEST)
