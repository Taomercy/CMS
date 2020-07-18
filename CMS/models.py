from django.db import models

# Create your models here.
from django.db.models import PROTECT


class Family(models.Model):
    # 家庭地址
    address = models.TextField()
    # 违章情况
    illegal_situation = models.TextField()
    # 商品房情况
    commercial_housing_situation = models.TextField()
    # 房屋出租情况
    rental_status = models.TextField()
    # 对象类别
    object_class = models.TextField()
    # 车辆情况
    vehicle_condition = models.TextField()

    @staticmethod
    def get_thread():
        return ["家庭地址", "违章情况", "商品房情况", "房屋出租情况", "对象类别", "车辆情况"]

    def __str__(self):
        return self.address


class Person(models.Model):
    # 称谓
    appellation = models.TextField()
    # 姓名
    name = models.TextField()
    # 户籍地
    domicile = models.TextField()
    # 家庭地址
    family = models.ForeignKey(Family, primary_key=False, blank=False, on_delete=PROTECT)
    # 工作单位
    work_units = models.TextField()
    # 身份证号
    id_number = models.TextField(unique=True)
    # 收入情况
    income = models.TextField()
    # 社会保障
    social_security = models.TextField()
    # 政治面貌
    political_landscape = models.TextField()
    # 健康状况
    health = models.TextField()
    # 联系电话
    phone_number = models.TextField()

    @staticmethod
    def get_thread():
        return ["称谓", "姓名", "户籍地", "工作单位", "身份证号", "收入情况", "社会保障", "政治面貌", "健康状况", "联系电话"]

    @staticmethod
    def get_simple_thead():
        return ["姓名", "身份证号", "联系电话", "家庭地址"]

    def __str__(self):
        return self.name


class HandleAffairsRecord(models.Model):
    # 事项
    event = models.TextField()
    # 经办人
    agent = models.TextField()
    # 时间
    create_at = models.DateTimeField(auto_created=True)

    @staticmethod
    def get_thread():
        return ["时间", "事项", "经办人", ]




