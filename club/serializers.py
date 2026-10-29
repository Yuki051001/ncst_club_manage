from rest_framework import serializers
from .models import Member, Department, Competition

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    # 为了让前端直接拿到部门的名字，而不是只拿到一个数字 ID
    department_name = serializers.CharField(source='department.name', read_only=True)
    role_display = serializers.CharField(source='get_role_display', read_only=True)

    class Meta:
        model = Member
        fields = '__all__'  # 包含 Member 表里的所有字段


class CompetitionSerializer(serializers.ModelSerializer):
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    participation_mode_display = serializers.CharField(source='get_participation_mode_display', read_only=True)

    class Meta:
        model = Competition
        fields = '__all__'