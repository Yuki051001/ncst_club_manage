from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member, Department, Competition

# @api_view(['GET'])
# def member_list(request):
#     members = Member.objects.all()
#     data = [{
#         'id': m.id,
#         'name': m.name,
#         'stu_id': m.stu_id,
#         'gender': m.gender,
#         'birth': m.birth,
#         'school': m.school,
#         'grade': m.grade,
#         'major': m.major,
#         'mobile': m.mobile,
#         'email': m.email,
#     }for m in members]

#     return Response({'code': 200, 'message': '获取成功', 'data': data})


from rest_framework import viewsets,filters
from .serializers import MemberSerializer, DepartmentSerializer, CompetitionSerializer


# 成员接口
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-id')
    serializer_class = MemberSerializer

# 部门接口
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    # 允许前端通过 ?search=xxx 搜索标题，或者 ?level=国家级 筛选
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category', 'host_unit']
    ordering_fields = ['registration_end', 'created_at']