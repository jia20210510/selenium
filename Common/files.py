# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: selenium
@File: files.PY
@Date: 2021/8/15 21:41
@Author: jia
@Description:
"""
# from pandas importread_csv
import csv
import os
import shutil


# 新建文件
def new_file(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        shutil.rmtree(dir_path)
        os.mkdir(dir_path)


# 查找根目录
def get_project_path(project_name):
    base = os.getcwd()
    root_path = base[:base.find(project_name+"\\") + len(project_name+"\\")]
    project_path = root_path.replace("\\", '/')
    return project_path


# 读取CSV文件
def read_file(f_path):
    with open(f_path, 'r', encoding='gbk') as rf:
        file_reader = csv.reader(rf)
        file_data = list(file_reader)
        return file_data


# def resd_file_2(f_path):
#     with open(f_path, encoding='UTF-8') as rrf:
#         names = ['作业日期', 'ηCO', 'ηH2', 'TF(℃)', 'TC(℃)', 'mass', '送风流量']
#         data = read_csv(rrf, names=names)

# 清除文件
def clear_file(f_path):
    with open(f_path, 'r+', encoding='utf-8') as cf:
        cf.truncate()


def write_file(file_path, write_text):
    with open(file_path, 'w', encoding='utf-8') as wf:
        wf.write(write_text)
