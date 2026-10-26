from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member

@api_view(['GET'])
def member_list(request):
    members = Member.objects.all()
    data = [{
        'id': m.id,
        'name': m.name,
        'stu_id': m.stu_id,
        'gender': m.gender,
        'birth': m.birth,
        'school': m.school,
        'grade': m.grade,
        'major': m.major,
        'mobile': m.mobile,
        'email': m.email,
    }for m in members]

    return Response({'code': 200, 'message': '获取成功', 'data': data})