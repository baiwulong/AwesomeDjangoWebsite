from django.shortcuts import render
from django.http import  HttpResponse


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

#添加抄牌警示
def add(request):
    return HttpResponse("add");

#删除抄牌警示
def remove(request):
    return HttpResponse("remove");

#抄牌警示列表
def list(request):
    return HttpResponse("list");









class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer