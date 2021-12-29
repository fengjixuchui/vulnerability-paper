#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import sys
import platform


def generate_wordlist_file(root_dir, dir_path='', word_list=[]):
    try:
        root_file_list = os.listdir(root_dir)
        for file in root_file_list:
            if file.startswith("."):
                root_file_list.remove(file)
            else:
                file_path = root_dir + '/' + file
                # 如果为文件则记录文件路径
                if os.path.isfile(file_path):
                    word_list.append(dir_path + '/' + file)
                # 如果为文件夹则递归
                elif os.path.isdir(file_path):
                    generate_wordlist_file(file_path, dir_path + '/' + file, word_list)
                else:
                    pass
    except Exception as e:
        print(e)

    finally:
        return word_list


def generate_wordlist_dir(root_dir, dir_path='', word_list=[]):
    try:
        root_file_list = os.listdir(root_dir)
        for file in root_file_list:
            if file.startswith("."):
                root_file_list.remove(file)
            else:
                file_path = root_dir + '/' + file
                # 如果为文件则记录文件路径
                if os.path.isfile(file_path):
                    # word_list.append(dir_path + '/' + file)
                    pass
                # 如果为文件夹则递归
                elif os.path.isdir(file_path):

                    generate_wordlist_dir(file_path, dir_path + '/' + file, word_list)
                else:
                    pass
    except Exception as e:
        print(e)

    finally:
        word_list.append(dir_path + '/')
        return word_list


if __name__ == '__main__':
    try:
        root_dir_path = sys.argv[1]
    except:
        print('无路径参数，默认为当前文件夹')
        root_dir_path = os.getcwd()
    finally:
        if os.path.isdir(root_dir_path):
            # print(platform.system() + platform.release())
            if platform.system() == 'Windows':
                # windows系统文件路径为 \\
                try:
                    dir_name = root_dir_path.split('\\')
                    length = len(dir_name)
                    file_name = dir_name[length - 1].strip()
                    # 做空值判断
                    if file_name == '':
                        file_name = dir_name[length - 2].strip()
                        if file_name == '':
                            file_name = 'word_list'
                    file_name_txt = file_name + '.txt'
                    file_path_txt = os.getcwd() + '\\' + file_name_txt
                    file_name_json = file_name + '.json'
                    file_path_json = os.getcwd() + '\\' + file_name_json

                    word_list_file = generate_wordlist_file(root_dir_path)
                    # 增加文件夹的路径列表
                    # word_list_dir = generate_wordlist_dir(root_dir_path)
                    # word_list = word_list_dir + word_list_file
                    # 这里去掉了文件夹路径
                    word_list = word_list_file

                    # 写入txt
                    with open(file_path_txt, 'w') as word_file:
                        for word in word_list:
                            word_file.write(word + '\n')
                    print(file_path_txt)

                    # 写入json
                    with open(file_path_json, 'w') as word_file:
                        word_file.write(json.dumps(word_list))
                    print(file_path_json)
                except:
                    pass
            elif platform.system() == 'Linux':
                # linux系统文件路径为 /
                try:
                    dir_name = root_dir_path.split('/')
                    length = len(dir_name)
                    file_name = dir_name[length - 1].strip()
                    # 做空值判断
                    if file_name == '':
                        file_name = dir_name[length - 2].strip()
                        if file_name == '':
                            file_name = 'word_list'
                    file_name_txt = file_name + '.txt'
                    file_path_txt = os.getcwd() + '/' + file_name_txt
                    file_name_json = file_name + '.json'
                    file_path_json = os.getcwd() + '/' + file_name_json

                    word_list_file = generate_wordlist_file(root_dir_path)
                    # 增加文件夹的路径列表
                    # word_list_dir = generate_wordlist_dir(root_dir_path)
                    # word_list = word_list_dir + word_list_file
                    # 这里去掉了文件夹路径
                    word_list = word_list_file


                    with open(file_path_txt, 'w') as word_file:
                        for word in word_list:
                            word_file.write(word + '\n')
                    print(file_path_txt)

                    # 写入json
                    with open(file_path_json, 'w') as word_file:
                        word_file.write(json.dumps(word_list))
                    print(file_path_json)

                except:
                    pass
            else:
                # 其他系统不作处理
                pass
        else:
            print('路径参数的指定路径不是文件夹(ps:无路径参数，默认为当前文件夹)')
