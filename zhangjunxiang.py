'''
Auther:WYF
Date:2019/08/03
Help:此工具用于处理zjx的某个任务，需要对一个大的文件夹下的各个子文件夹内的文件进行处理，找出其中的IP/MASK字段，写入该子文件夹
    下的汇总文件中。
'''
import os
import re
from re_list import match_ip_and_mask


# sub_dir_path
def sub_dir_path(folder):
    path = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'), folder)
    name = os.listdir(path)
    dir_path = list(map(lambda x: os.path.join(path, x), name))
    return dir_path


# file_path
def file_path(dir_path):
    name = list(map(lambda x: os.path.join(dir_path, x), os.listdir(dir_path)))
    return name


# create summary file
def create_summary_file(name, path, content):
    summary_file_name = os.path.join(path, name)
    f = open(summary_file_name, 'a+', encoding='utf-8')
    for i in content:
        f.write(i + '\n')
    f.close()
    print("%s is done." % summary_file_name)


# match ip
def match_ip(file, zz):
    pp = re.compile(zz)
    f = open(file, 'r', encoding='utf-8')
    # f = open(file, 'r')
    con = f.readlines()
    f.close()
    match = [pp.search(i).group() for i in con if pp.search(i)]
    return match


# main
if __name__ == '__main__':
    folder_name = input("文件夹：")
    summary_name = 'summary.txt'
    for dir_name in sub_dir_path(folder_name):
        file_name = file_path(dir_name)
        for files in file_name:
            print("开始处理%s。" % os.path.join(dir_name, files))
            create_summary_file(summary_name, dir_name, match_ip(files, match_ip_and_mask()))
            print("%s处理结束。" % os.path.join(dir_name, files))
    print("All messions are completed.")
    os.system('pause')
