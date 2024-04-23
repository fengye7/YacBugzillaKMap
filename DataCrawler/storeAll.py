import django
import os
import sys

# 设置Django环境
sys.path.append('D:\\Files\\Code\\CoursesProjects\\YacBugzilla_KnowledgeMap')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YacBugzilla_KnowledgeMap.settings')
django.setup()

import pandas as pd
from RecordsHandler.models import Reported,Modified
from DataHandler.models import BugTuple
from CommentHandler.models import Comment
from datetime import datetime

Date_Format1 = "%Y-%m-%d %H:%M %Z"
Date_Format2 = "%Y-%m-%d %H:%M:%S %Z"

def storeReported():
    file_path = "./data/bug__reported.xlsx"  # 定义Excel文件路径
    
    # 读取Excel文件数据
    df = pd.read_excel(file_path)
    
    # 遍历每一行数据
    for index, row in df.iterrows():
        id = row['ID']  # 从Excel中获取Bug ID
        user = row['User']  # 从Excel中获取User
        time = datetime.strptime(row['Time'], Date_Format1) # 从Excel中获取Time
        bugId = row['BugId'] # 从Excel中获取BugId

        # 创建Reported模型实例并存入数据
        reported = Reported(
            id= id,
            user=user,
            time=time,
            bugId=bugId,
        )

        # 保存数据到数据库
        reported.save()
        print(id,"reported has been stored")

    print('Data imported successfully')

def storeModified():
    file_path = "./data/bug__modified.xlsx"  # 定义Excel文件路径
    
    # 读取Excel文件数据
    df = pd.read_excel(file_path)
    
    # 遍历每一行数据
    for index, row in df.iterrows():
        id = row['ID']  # 从Excel中获取Bug ID
        user = row['User']  # 从Excel中获取User
        time = datetime.strptime(row['Time'], Date_Format2) # 从Excel中获取Time
        bugId = row['BugId'] # 从Excel中获取BugId

        # 创建Modified模型实例并存入数据
        modified = Modified(
            id= id,
            user=user,
            time=time,
            bugId=bugId,
        )

        # 保存数据到数据库
        modified.save()
        print(id,"modified has been stored")

    print('Data imported successfully')

def storeBugTuple():
    file_path = "./data/bug_data.xlsx"  # 定义Excel文件路径
    
    # 读取Excel文件数据
    df = pd.read_excel(file_path)
    
    # 遍历每一行数据
    for index, row in df.iterrows():
        id = row['ID']
        product = row['Product'] 
        component = row['Component']
        assignee = row['Assignee']
        status = row['Status']
        summary = row['Summary']
        version =row['Version']
        platform = row['Platform']
        op_sys = row['Op_sys']
        priority = row['Priority']
        severity = row['Severity']
        QA = row['QA']
        ccList = row['CCList']
        reportedId = row['ReportedId']

        # 创建BugTuple模型实例并存入数据
        bug = BugTuple(
            id = id,
            product =product,
            component = component,
            assignee = assignee,
            status = status,
            summary = summary,
            version = version,
            platform = platform,
            op_sys = op_sys,
            priority = priority,
            severity = severity,
             QA=QA,
            ccList = ccList,
            reportedId = reportedId,
        )

        # 保存数据到数据库
        bug.save()
        print(id,"bugTuple has been stored")

    print('Data imported successfully')

def storeComments():
    file_path = "./data/bug__comment(1).xlsx"  # 定义Excel文件路径
    
    # 读取Excel文件数据
    df = pd.read_excel(file_path)
    
    # 遍历每一行数据
    for index, row in df.iterrows():
        id = row['ID']
        commentator = row['Commentator'] 
        content = row['Content']
        time = datetime.strptime(row['Time'], Date_Format2) # 从Excel中获取Time
        bugId = row['BugId']        

        # 创建Comment模型实例并存入数据
        comment = Comment(
            id=id,
            commentator=commentator,
            content=content,
            time=time,
            bugId=bugId,
            )

        # 保存数据到数据库
        comment.save()
        print(id,"comment has been stored")

    print('Data imported successfully')

# Reported.objects.all().delete()
# storeReported()
# storeReported()
# storeModified()
# storeBugTuple()
storeComments()