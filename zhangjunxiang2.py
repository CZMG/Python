'''
Auther:WYF
Date:2019/08/03
Help:此工具用于处理zjx的某个任务。需要对一个大的文件夹下的各个子文件夹内的文件进行处理，找出其中的第一个IP-IP字段，写入该子文件夹
    下的汇总文件中。
'''
import os
from re_list import match_ip_range
from zhangjunxiang import sub_dir_path, file_path, create_summary_file, match_ip

# main
if __name__ == '__main__':
    folder_name = input("文件夹：")
    summary_name = 'result.txt'
    for dir_name in sub_dir_path(folder_name):
        file_name = file_path(dir_name)
        for files in file_name:
            if files.endswith('新建文本文档.txt'):
                print("开始处理%s。" % os.path.join(dir_name, files))
                create_summary_file(summary_name, dir_name, match_ip(files, match_ip_range()))
                print("%s处理结束。" % os.path.join(dir_name, files))
                os.remove(files)
            if files.endswith('summary.txt'):
                os.remove(files)
    print("All messions are completed.")
    os.system('pause')
