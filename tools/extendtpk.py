# ------------------------------------------------------------------------------
# python extendtpk.py
# This function increase the zoom level for Esri SDK TPK to 20
# It require to have the file in the same directory. 
# The function will extract the TPK and then alter the max zoom level to 20.
# 
# Creator : Sulaiman Mukahhal
# Project : Open IMSMA Project - GICHD
# ------------------------------------------------------------------------------
#!/usr/bin/env python
# coding: utf-8


import argparse
from zipfile import ZipFile
import os, os.path
import json

def check_is_file(zipfile):
    counter = 0
    zipfile_name = zipfile.split('.')
    file_name = zipfile_name[0]
    file_extension = zipfile_name[1]
    if os.path.isfile(file_name):
        while os.path.isfile('{}_{}.{}'.format(file_name, counter, file_extension)):
            counter +=1
        zipfile = '{}_{}.{}'.format(file_name, counter, file_extension)
    return zipfile



def create_directory(directory):
    counter = 0
    if os.path.isdir(directory):
        while os.path.isdir('{}_{}'.format(directory, counter)):
            counter+=1
        directory = '{}_{}'.format(directory, counter)
        os.mkdir(directory)
    else:
        os.mkdir(directory)
    print('directory {} created!'.format(directory))
    return directory
        

def get_all_file_paths(directory):
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        print(root)
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths       


def unzip_main(file_name):
    # get file name and the directory name
    directory = file_name.split('.')[0]
    cwd = os.getcwd()
    print(file_name)
    print(directory)
    print(cwd)

    # create diretory with the same name as the file
    directory = create_directory(directory)
    print(directory)
    with ZipFile(file_name, 'r') as zip:
        os.chdir(directory)
        zip.extractall()
        os.chdir(cwd)
        # print('done!')
    return directory
    

def main(tpk_file, directory):
    # path to folder which needs to be zipped 
    tpk_file = check_is_file(tpk_file)
    # calling function to get all file paths in the directory 
    file_paths = get_all_file_paths(directory)
    
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
        
    # writing files to a zipfile 
    with ZipFile(tpk_file,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 
  
    print('All files zipped successfully!')   




if __name__ == "__main__": 
    # path to folder which needs to be zipped 
    tpk_file = 'dink.tpk'
    directory = unzip_main(tpk_file)
    print(directory)
    with open('{}/servicedescriptions/mapserver/mapserver.json'.format(directory)) as json_file:
        data = json.load(json_file)

    print(data["contents"]["maxScale"])
    print(type(data["contents"]["maxScale"]))
    data["contents"]["maxScale"] = 564.248588000000041
    print(data["contents"]["maxScale"])

    with open('{}/servicedescriptions/mapserver/mapserver.json'.format(directory), 'w') as out_file:
        json.dump(data, out_file)
    main(tpk_file, directory) 









