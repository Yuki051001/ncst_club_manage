from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=8,verbose_name="姓名")
    stu_id = models.CharField(max_length=12,unique=True,verbose_name="学号")
    gender = models.CharField(max_length=1,choices=[("M","男"),("F","女"),("O","二次元")],verbose_name="性别")
    birth = models.DateField(blank=True,null=True,verbose_name="出生日期")
    school= models.CharField(max_length=20,default="华北理工大学（曹妃甸校区）",verbose_name="学校")
    grade = models.CharField(max_length=4,verbose_name="年级")
    major = models.CharField(max_length=15,verbose_name="专业")
    mobile = models.CharField(max_length=11,unique=True,verbose_name="手机号")
    email = models.EmailField(unique=True,verbose_name="邮箱")
    role = models.CharField(
        max_length=20,
        choices=[("president","会长"),("vice_president","副会长"),("leader","部长"),("vice_leader","副部长"),("member","成员")],
        default="member",
        verbose_name="职位"
    )

    # 关联部门表
    department = models.ForeignKey(
        "Department",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="所属部门"
        )



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "成员"
        verbose_name_plural = verbose_name


class Department(models.Model):
    name = models.CharField(max_length=10,unique=True,verbose_name="部门名称")
    description = models.TextField(blank=True,verbose_name="部门简介")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name