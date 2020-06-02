#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

#Функция ищет все файлы с именем filename во всех подкаталогах каталога catalog


def find_files(catalog):
    find_files = []
    v = []
    v = find_files
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files]
    clear_files(find_files)
    del_files(find_files)
    #V1.0
    #shutil.rmtree(catalog)
    #os.rmdir(catalog)
    return v


def clear_files(find_files):
    for file in find_files:
        with open ('{}'.format(file), 'wb'):
            pass
    print("All TXT are vanished")


def del_files(find_files):
    for file in find_files:
        os.remove(file)
    print("All TXT are deleted")



if __name__=='__main__':
    v = find_files(catalog= r'C:\Users\Nikita\PycharmProjects\total_cleaner\s')
    print(v)
    #print(find_files(sys.argv[1]))


