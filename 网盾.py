# -*- coding: utf-8 -*-
'''
用于在桌面上新建一个文件夹，并在文件夹中创建数个网盾中的项目文件夹，
以及其内5个存放不同项目文件的子文件夹。
'''

import os
import time


def mkdir_dir(num):
    path_desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    dir_name = time.strftime("%Y%m%d", time.gmtime())
    dir_path = os.path.join(path_desktop, dir_name)
    os.mkdir(dir_path)
    sub_dir_name = ["Project"+str(i) for i in range(1,num + 1)]
    for sub_name in sub_dir_name:
        sub_dir_path = os.path.join(dir_path, sub_name)
        os.mkdir(sub_dir_path)
        for file_name in project_file_dir:
            file_dir_path = os.path.join(sub_dir_path, file_name)
            os.mkdir(file_dir_path)
    return print('文件夹创建完毕。')

project_file_dir = ["安全验收报告", "风险评估报告", "项目建议书", "扫描文件", "附件"]

if __name__ == '__main__':
    number = int(input("项目个数：\n>>>"))
    mkdir_dir(number)
    os.system("pause")