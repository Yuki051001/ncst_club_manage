from django.db import models

# Create your models here.
# 协会成员模型
class Member(models.Model):
    name = models.CharField(max_length=8,verbose_name="姓名")
    stu_id = models.CharField(max_length=12,unique=True,verbose_name="学号")
    gender = models.CharField(max_length=1,choices=[("M","男"),("F","女"),("O","二次元")],verbose_name="性别")
    birth = models.DateField(blank=True,null=True,verbose_name="出生日期")
    school = models.CharField(max_length=20,default="华北理工大学（曹妃甸校区）",verbose_name="学校")
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

# 部门模型
class Department(models.Model):
    name = models.CharField(max_length=10,unique=True,verbose_name="部门名称")
    description = models.TextField(blank=True,verbose_name="部门简介")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name


class Competition(models.Model):
    # 基础信息
    title = models.CharField(max_length=50,verbose_name="竞赛名称")
    description = models.TextField(blank=True,verbose_name="竞赛简介")
    location = models.CharField(max_length=100, blank=True, verbose_name="比赛地点")
    registration_link = models.URLField(blank=True, verbose_name="报名链接")

    # 时间节点
    registration_start = models.DateTimeField(verbose_name="报名开始时间")
    registration_end = models.DateTimeField(verbose_name="报名结束时间")
    submission_deadline = models.DateTimeField(null=True, blank=True, verbose_name="提交作品截止时间")

    # 竞赛类型级别
    LEVEL_CHOICES = (('国家级', '国家级'), ('省级', '省级'), ('校级', '校级'))
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="竞赛级别")

    category = models.CharField(max_length=50, verbose_name="竞赛大类")
    comp_type = models.CharField(max_length=20, blank=True, verbose_name="竞赛类型")

    host_unit = models.CharField(max_length=50, blank=True, verbose_name="负责单位")
    school_unit = models.CharField(max_length=50, blank=True, verbose_name="校内组织单位")
    recognized_level = models.CharField(max_length=20, blank=True, verbose_name="认定等级")
    is_recognized = models.BooleanField(default=False, verbose_name="是否高等协会认可")
    
    manager_name = models.CharField(max_length=20, blank=True, verbose_name="负责人")
    manager_phone = models.CharField(max_length=15, blank=True, verbose_name="负责人联系电话")

    PART_MODE_CHOICES = (('个人', '个人'), ('团队', '团队'))
    participation_mode = models.CharField(max_length=10, choices=PART_MODE_CHOICES, default='个人', verbose_name="参赛方式")
    fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, verbose_name="报名费")
    
    requires_work = models.BooleanField(default=False, verbose_name="是否需要作品")
    need_bank_card = models.BooleanField(default=False, verbose_name="是否收集银行卡号")
    allow_mentor = models.BooleanField(default=True, verbose_name="允许自主选导师")

    # 官方文件
    host_notice_file = models.FileField(upload_to='competitions/notices/', blank=True, null=True, verbose_name="主办方通知文件")
    school_notice_file = models.FileField(upload_to='competitions/school_notices/', blank=True, null=True, verbose_name="校内赛通知")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "竞赛"
        verbose_name_plural = verbose_name

