# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class EduRankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field() # 岗位名称
    companyName = Field() # 招聘单位
    recruitment = Field() # 招聘人数
    province  = Field() # 省
    city  = Field() # 市
    county = Field() # 县
    jurisdictionCode = Field()# 辖区代码
    jobCode = Field()# 岗位代码
    section = Field() # 学段
    subject = Field() #  学科
    singleLinePlan = Field() # 单列计划
    educationLimit = Field() # 学历限制
    isDegree = Field() # 是否需要学位
    ageLimit = Field() # 年龄限制
    professionLimit = Field() # 专业限制
    censusLimit = Field() # 户籍限制
    isCertificate = Field() # 是否教师资格证
    remarks = Field() # 备注
    score = Field() # 成绩
    high = Field() # 最高分
    medium = Field() # 小围分
    low = Field()   # 入围分
    # 只展示当年
    register = Field() # 报名人数
    payer = Field() # 缴费人数
    year = Field() # 年份

